"""
A NON-ASYNC server for the game Tic Tac Toe.
This will, unfortunately, support only one game at a time.

Features:
    Supports variable game board length
    Supports multiple players
"""
import argparse
import socket
import time
import select
from constants import TicTacToeRows, MAX_TIC_TAC_TOE_PLAYERS, TIC_TAC_TOE_SYMBOLS



# TODO: Env variables


class PlayerDisconnectError(Exception):
    pass


def main():
    parser = argparse.ArgumentParser(description='Run a Tic Tac Toe game server')
    parser.add_argument('board_x_size', metavar='X', type=int, nargs='?', default=3,
                        help='The horizontal size of the board')
    parser.add_argument('board_y_size', metavar='Y', type=int, nargs='?', default=3,
                        help='The vertical size of the board')
    parser.add_argument('needed_symbols', metavar='Z', type=int, nargs='?', default=3,
                        help='The number of consecutive symbols that account for a winning move.')
    parser.add_argument('player_count', metavar='P', type=int, nargs='?', default=2,
                        help='The number of players.', choices=range(2, 10))
    args = parser.parse_args()

    server = GameServer(player_count=args.player_count, board_x_size=args.board_x_size,
                        board_y_size=args.board_y_size, needed_symbols=args.needed_symbols)
    try:
        server.start()
    finally:
        server.close_connections()


class Server:
    """ The base server class, which listens on a socket and accepts connections """
    def __init__(self, max_connections: int):
        self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(f'Hostname is {socket.gethostname()}')
        self.serversocket.bind((socket.gethostname(), 4325))
        self.serversocket.listen(max_connections)
        self.max_connections = max_connections
        self.connections: [(socket.socket, str)] = []  # hold the socket connections
        self.accept_connections = True

    def start(self):
        """
        Accept connections until we get filled up
        :return:
        """
        while self.accept_connections:
            self.accept_connection()
            if len(self.connections) >= self.max_connections:
                break

    def accept_connection(self):
        clientsocket, address = self.serversocket.accept()
        print(f'Accepted a player - {clientsocket} @ {address}')
        self.connections.append((clientsocket, address))

    def close_connections(self):
        for conn, _ in self.connections:
            conn.close()
        self.serversocket.detach()
        self.serversocket.close()
        print('Closed connections!')


class GameServer(Server):
    def __init__(self, player_count: int, board_x_size: int=3, board_y_size: int=3, needed_symbols: int=3):
        super().__init__(player_count)
        if not TicTacToe.is_valid_board_size(board_x_size, board_y_size, needed_symbols):
            raise Exception('Invalid board size/needed symbols!')
        self.board_x_size = board_x_size
        self.board_y_size = board_y_size
        self.needed_symbols = needed_symbols
        self.players = []
        self.player_turn_idx = 0  # TODO: Random

    def accept_connection(self):
        """
        Create the Player objects and fill up your self.players list
        """
        super().accept_connection()
        current_connection = self.connections[-1]
        current_player = Player(current_connection[0])
        self.players.append(current_player)
        if len(self.players) == self.max_connections:
            # this is the second player, therefore we can start the game
            self.start_game()
        else:
            # the first player connected, send him a message to wait
            current_player.send_message(f"Welcome to the game. {len(self.players)}/{self.max_connections} players waiting for a game\nPlease wait while enough players connect...")

    def start_game(self):
        """
        The main game loop
        """
        self.set_player_symbols()

        game: TicTacToe = TicTacToe(self.players, board_x_size=self.board_x_size, board_y_size=self.board_y_size,
                                    needed_symbols=self.needed_symbols)

        self.send_message_to_players('The game has started!')
        time.sleep(0.1)
        self.send_message_to_players(game.get_board_state())
        time.sleep(0.1)

        while True:
            active_player: Player = self.players[self.player_turn_idx]
            active_player.send_message('\nIt is your turn! Please choose a valid position')
            active_player.send_message(f'\nValid positions: {game.get_empty_positions()}')

            chosen_position = active_player.receive_message()
            try:
                self._check_players()
            except PlayerDisconnectError as dc_e:
                # A player has disconnected, stop the game
                self.send_message_to_players(f"\n {str(dc_e)}\nThe game will now end.")
                return

            is_valid_turn = game.is_valid_position(*[int(p) for p in chosen_position.decode().split()])
            # TODO: validate position

            if is_valid_turn:
                game_has_ended = self.handle_valid_turn(game, [int(p) for p in chosen_position.decode().split()])
                if game_has_ended:
                    return

    def handle_valid_turn(self, game: 'TicTacToe', chosen_position: (int, int)) -> bool:
        """
        :return: A boolean indicating if the game has ended or not
        """
        game.move_position(chosen_position)

        self.player_turn_idx += 1
        if self.player_turn_idx == len(self.players):
            self.player_turn_idx = 0

        if game.has_ended():
            if game.winner is None:
                # Stalemate
                self.send_message_to_players("The game has ended in a stalemate!")
            else:
                game.winner.send_message('You have won the game!')
                gw_idx = self.players.index(game.winner)
                self.send_message_to_players('You have lost the game.', excluding=gw_idx)
        else:
            # print the board to the players
            self.send_message_to_players(game.get_board_state())

        return game.has_ended()

    def _check_players(self):
        # Check if every player is still connected
        for idx, pl in enumerate(self.players):
            r, w, e = select.select([pl.connection], [], [], 0)
            if r:
                data = pl.connection.recv(1024)
                if len(data) == 0:
                    raise PlayerDisconnectError(f'Player #{idx} has disconnected!')

    def set_player_symbols(self):
        """ Sets the symbols of the players"""
        for idx, player in enumerate(self.players):
            player.set_symbol(TIC_TAC_TOE_SYMBOLS[idx])

    def send_message_to_players(self, message: str, excluding: int=-1):
        """
        :param excluding: int index pointing out to which player NOT to send the mssage
        """
        for i in range(len(self.players)):
            if i != excluding:
                self.players[i].send_message(message)


class Player:
    def __init__(self, connection: socket.socket):
        self.connection: socket.socket = connection
        self.symbol = None

    def set_symbol(self, smb):
        self.symbol = smb

    def send_message(self, msg: str):
        self.connection.send(bytes(msg, encoding='utf-8'))

    def receive_message(self):
        while True:
            r, w, e = select.select([self.connection], [], [], 0.1)
            if r:
                message = self.connection.recv(1024)
                return message

    def __eq__(self, other):
        return self.connection == other.connection

    def __hash__(self):
        return hash(self.connection.getsockname())


class TicTacToe:
    """ TicTacToe game between two players """

    valid_winning_rows = [row.value for row in TicTacToeRows]

    def __init__(self, players: [Player], board_x_size=3, board_y_size=3, needed_symbols=3):
        if not self.is_valid_board_size(board_x_size, board_y_size, needed_symbols):
            raise Exception('Invalid board size/needed symbols!')
        self.board = self._build_board(board_x_size, board_y_size)
        self.empty_positions = self._get_empty_positions()
        self.active_player_idx = 0
        self.players = players
        self._game_has_ended = False
        self.needed_symbols = 3  # the number of consecutive symbols needed to win the game
        self.MAX_X, self.MAX_Y = len(self.board), len(self.board[0])
        self.winner = None

    def _build_board(self, x_size, y_size):
        """
        Builds a matrix representing the board
        """
        return [['[ ]' for _ in range(y_size)] for _ in range(x_size)]

    def _get_empty_positions(self) -> {(int, int)}:
        """
        Iterates through the board and returns a set of tuples, representing all the empty positions on the board
        """
        empty_positions = set()
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                empty_positions.add((row, col))
        return empty_positions

    @staticmethod
    def is_valid_board_size(x_size, y_size, needed_symbols):
        return not (x_size <= 0 or y_size <= 0 or needed_symbols <= 0 or needed_symbols > min(x_size, y_size))

    def get_board_state(self) -> str:
        return ''.join('\n'.join([''.join(row) for row in self.board]))

    def get_empty_positions(self) -> {(int, int)}:
        """ Returns all the empty positions on the board """
        return self.empty_positions

    def is_valid_position(self, x, y):
        return (0 <= x < len(self.board) and 0 <= y < len(self.board[0])
                and self.board[x][y] == '[ ]')

    def move_position(self, pos: (int, int)):
        if not self.is_valid_position(*pos):
            raise Exception('Invalid Position!')
        elif self._game_has_ended:
            raise Exception('The game has ended, you cannot make more moves!')

        x, y = pos
        active_player = self.players[self.active_player_idx]
        self.board[x][y] = '[' + active_player.symbol + ']'
        self.empty_positions.remove((x, y))
        self.check_game_end(x, y)

        self.active_player_idx += 1
        if self.active_player_idx == len(self.players):
            self.active_player_idx = 0

    def check_game_end(self, x, y):
        """ Checks if a winning move has been made"""
        for valid_row in self.valid_winning_rows:
            direction_one, direction_two = valid_row
            row_symbols_count = (  # the number of consecutive symbols in the given row
                self.__get_consecutive_symbols_count(x, y, direction=direction_one.value)
              + self.__get_consecutive_symbols_count(x, y, direction=direction_two.value)
              + 1
            )
            if row_symbols_count >= self.needed_symbols:
                # The game has ended, whoever's turn is has losts!
                self._game_has_ended = True
                self.winner = self.players[self.active_player_idx]
                return
        if len(self.empty_positions) == 0:
            # Theere are no moves to be made and we have not found a winner,
            # therefore this is a stalemate
            self._game_has_ended = True
            self.winner = None

    def has_ended(self):
        return self._game_has_ended

    def __get_consecutive_symbols_count(self, start_x: int, start_y: int, direction: (int, int)):
        dir_x, dir_y = direction
        orig_symbol = self.board[start_x][start_y]
        symbol_count = 0
        curr_x, curr_y = start_x + dir_x, start_y + dir_y
        # Traverse to the direction until we go out of bounds or find a different symbol
        while 0 <= curr_x < self.MAX_X and 0 <= curr_y < self.MAX_Y and self.board[curr_x][curr_y] == orig_symbol:
            symbol_count += 1
            curr_x += dir_x
            curr_y += dir_y

        return symbol_count


if __name__ == '__main__':
    main()
