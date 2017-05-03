import socket
import time


def receive_message(socket):
    message = socket.recv(2000)
    print(message)

    while not message:
        time.sleep(1)
        message = socket.recv(2000)
        print(message)

    return message

ps: socket.socket = socket.create_connection(('Netherbook', 4327))

while True:
    msg = receive_message(ps)
    print()

    if 'Valid positions:' in msg.decode():
        ps.send(bytes(input(), encoding='utf-8'))
