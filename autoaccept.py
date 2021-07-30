import time
from lcu_driver import Connector

connector = Connector()
async def accept(connection):
    while True:
        request = await connection.request('get', '/lol-matchmaking/v1/ready-check')
        fila = await request.json()


        if fila['state'] == 'InProgress':
            aceitar = await connection.request('post', '/lol-matchmaking/v1/ready-check/accept')
            print('A partida foi aceita.')
            break

        time.sleep(2)

@connector.ready
async def connect(connection):
    print('Use se já está na fila')
    inicia_accept = input('Quer iniciar o autoaccept? \n( 0 = Não )\n( 1 = Sim )\n ')

    if inicia_accept == '1':
        print('Autoaccept iniciado!')
        await accept(connection)


connector.start()
