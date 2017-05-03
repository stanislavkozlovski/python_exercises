"""
A NON-ASYNC server for the game Tic Tac Toe.
This will, unfortunately, support only two players at a time.
"""
import socket
import time
from constants import TicTacToeRows

# TODO: Handle stalemate
def main():
    server = GameServer()
    try:
        server.start()
    finally:
        server.close_connections()


class Server:
    def __init__(self):
        self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(f'Hostname is {socket.gethostname()}')
        self.serversocket.bind((socket.gethostname(), 4327))
        self.serversocket.listen(5)
        self.connections: [(socket.socket, str)] = []  # hold the socket connections
        self.accept_connections = True
        self.max_connections = 5

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
        self.serversocket.close()
        print('Closed connections!')


class GameServer(Server):
    def __init__(self):
        super().__init__()
        self.players = []
        self.max_connections = 2

    def accept_connection(self):
        super().accept_connection()
        current_connection = self.connections[-1]
        current_player = Player(current_connection[0])
        self.players.append(current_player)
        if len(self.players) == 2:
            # this is the second player, therefore we can start the game
            self.start_game(self.players[0], self.players[1])

        else:
            # the first player connected, send him a message to wait
            current_player.send_message("Welcome to the game. Please wait while a second player connects...")

    def start_game(self, player_one: 'Player', player_two: 'Player'):
        is_player_one_turn = True
        is_valid_turn = True
        player_one.set_symbol('X')
        player_two.set_symbol('O')
        game: TicTacToe = TicTacToe(player_one, player_two)
        game_start_message = 'The game has started!'
        player_one.send_message(game_start_message)
        player_two.send_message(game_start_message)
        player_one.send_message(game.get_board_state())
        player_two.send_message(game.get_board_state())
        while True:
            active_player: Player = player_one if is_player_one_turn else player_two

            active_player.send_message('It is your turn! Please choose a valid position')
            active_player.send_message(f'Valid positions: {game.get_empty_positions()}')

            chosen_position = active_player.receive_message()
            is_valid_turn = game.is_valid_position(*[int(p) for p in chosen_position.decode().split()])
            # TODO: validate position
            if is_valid_turn:
                game.move_position(tuple([int(p) for p in chosen_position.decode().split()]))
                is_player_one_turn = not is_player_one_turn

                if game.has_ended():
                    game.winner.send_message('You have won the game!')
                    return
                # print the board to both players
                player_one.send_message(game.get_board_state())
                player_two.send_message(game.get_board_state())


class Player:
    def __init__(self, connection: socket.socket):
        self.connection: socket.socket = connection
        self.symbol = None

    def set_symbol(self, smb):
        self.symbol = smb

    def send_message(self, msg: str):
        self.connection.send(bytes(msg, encoding='utf-8'))

    def receive_message(self):
        message = self.connection.recv(100)
        while not message:
            time.sleep(1)
            message = self.connection.recv(100)
        return message

    def __eq__(self, other):
        return self.connection == other.connection

    def __hash__(self):
        return hash(self.connection.getsockname())


class TicTacToe:
    """ TicTacToe game between two players """

    valid_winning_rows = [row.value for row in TicTacToeRows]

    def __init__(self, player_one: Player, player_two: Player, board_x_size=3, board_y_size=3, needed_symbols=3):
        if not self._is_valid_board_size(board_x_size, board_y_size, needed_symbols):
            raise Exception('Invalid board size/needed symbols!')
        self.player_one = player_one
        self.player_two = player_two
        self.board = self._build_board(board_x_size, board_y_size)
        self.empty_positions = self._get_empty_positions()
        self.is_player_one_turn = True
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

    def _is_valid_board_size(self, x_size, y_size, needed_symbols):
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
        x, y = pos
        active_player = self.player_one if self.is_player_one_turn else self.player_two
        self.board[x][y] = '[' + active_player.symbol + ']'
        self.empty_positions.remove((x, y))
        self.is_player_one_turn = not self.is_player_one_turn

        self.check_game_end(x, y)

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
                self.winner = self.player_two if self.is_player_one_turn else self.player_one
                return

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
