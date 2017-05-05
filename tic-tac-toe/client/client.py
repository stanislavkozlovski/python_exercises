# import socket
# import time
# import select
from settings import HOSTNAME, PORT
# TIMEOUT_SECONDS = 0.1
#
# while True:
#     # See if the socket is marked as having data ready.
#     received, *_ = select.select([connection], [], [], TIMEOUT_SECONDS)
#     if received:
#         rec_data = connection.recv(1024)
#         msg = rec_data.decode()
#         print(msg)
#
#         # Length of zero ==> connection closed.
#         if len(rec_data) == 0:
#             cancelled = True
#             break
#
#         if 'Valid positions:' in msg:
#             connection.send(bytes(input(), encoding='utf-8'))
from curio import run, spawn
from curio.socket import *


async def play_game(client, addr):
    print('Connection from', addr)
    async with client:
        while True:
            data = await client.recv(1000)
            if not data:
                break

            msg = data.decode()
            if 'Are you alive' in msg:
                await client.sendall(bytes('Yes', encoding='utf-8'))
                continue
            print(msg)

            if 'Valid positions:' in msg:
                await client.sendall(bytes(input(), encoding='utf-8'))


    print('Connection closed')

async def main():
    client = await create_connection((HOSTNAME, PORT))
    await play_game(client, HOSTNAME)
if __name__ == '__main__':
    run(main)

