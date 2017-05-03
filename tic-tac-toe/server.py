import socket
"""
A NON-ASYNC server for the game Tic Tac Toe.
This will, unfortunately, support only two players at a time.
"""


def main():
    server = Server()

    try:
        server.start()
    finally:
        server.close_connections()


class Server:
    def __init__(self):
        self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(f'Hostname is {socket.gethostname()}')
        self.serversocket.bind((socket.gethostname(), 4317))
        self.serversocket.listen(5)

    def start(self):
        while True:
            self.accept_connection()

    def accept_connection(self):
        (clientsocket, address) = self.serversocket.accept()
        print(f'Accepted a player - {clientsocket} @ {address}')

    def close_connections(self):
        self.serversocket.close()
        print('Closed connections!')

if __name__ == '__main__':
    main()
