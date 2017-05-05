from curio import run, spawn
from curio.socket import *

from settings import HOSTNAME, PORT
# TIMEOUT_SECONDS = 0.1


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

    print('Game has ended')

async def main():
    client = await create_connection((HOSTNAME, PORT))
    await play_game(client, HOSTNAME)


if __name__ == '__main__':
    run(main)
