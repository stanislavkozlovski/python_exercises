"""
A NON-ASYNC server for the game Tic Tac Toe.
This will, unfortunately, support only two players at a time.
"""
import socket
import time

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
        self.serversocket.bind((socket.gethostname(), 4323))
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
                # print the board to both players
                player_one.send_message(game.get_board_state())
                player_two.send_message(game.get_board_state())


class Player:
    def __init__(self, connection: socket.socket):
        self.connection = connection
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


class TicTacToe:
    """ TicTacToe game between two players """
    def __init__(self, player_one: Player, player_two: Player):
        self.player_one = player_one
        self.player_two = player_two
        self.board = [
            ['[ ]', '[ ]', '[ ]'],
            ['[ ]', '[ ]', '[ ]'],
            ['[ ]', '[ ]', '[ ]']
        ]
        self.empty_positions = {
            (0, 0), (0, 1), (0, 2),
            (1, 0), (1, 1), (1, 2),
            (2, 0), (2, 1), (2, 2)
        }
        self.is_player_one_turn = True

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


if __name__ == '__main__':
    main()
