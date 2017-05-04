import socket
import time
import select


ps: socket.socket = socket.create_connection(('Netherbook', 4325))

while True:
    # See if the socket is marked as having data ready.
    r, w, e = select.select([ps], [], [], 0.1)
    if r:
        # msg = receive_message(ps).decode()
        data = ps.recv(1024)
        msg = data.decode()
        print(msg)

        # Length of zero ==> connection closed.
        if len(data) == 0:
            cancelled = True
            break

        if 'Valid positions:' in msg:
            ps.send(bytes(input(), encoding='utf-8'))
