import socket
import time


def receive_message(socket):
    message = socket.recv(100)
    while not message:
        time.sleep(1)
        message = socket.recv(100)
    return message

ps = socket.create_connection(('Netherbook', 4317))
print(receive_message(ps))