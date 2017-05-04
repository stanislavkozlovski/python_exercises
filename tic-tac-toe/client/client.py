import socket
import time
import select
from settings import HOSTNAME, PORT

TIMEOUT_SECONDS = 0.1
connection: socket.socket = socket.create_connection((HOSTNAME, PORT))

while True:
    # See if the socket is marked as having data ready.
    received, *_ = select.select([connection], [], [], TIMEOUT_SECONDS)
    if received:
        rec_data = connection.recv(1024)
        msg = rec_data.decode()
        print(msg)

        # Length of zero ==> connection closed.
        if len(rec_data) == 0:
            cancelled = True
            break

        if 'Valid positions:' in msg:
            connection.send(bytes(input(), encoding='utf-8'))
