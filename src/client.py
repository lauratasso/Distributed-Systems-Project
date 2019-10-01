import socket
from threading import Thread
import json

from classes.screen import Screen
from classes.ball import Ball

from utils.message_type import MessageTypes

# Inicializa tela e thread do servidor, além de adcionar bolas na tela


def startGame(data):
    global screen
    global thread_conn

    screen = Screen()

    for value in data.values():
        ball = Ball(tuple(value[0]), value[1], value[2])
        screen.ball_list.append(ball)

    # Inicializa thread do servidor
    thread_conn = Thread(target=server_thread)
    thread_conn.start()

    # Inicializa tela
    screen.run()

# Thread dedicada para comunicação com o servidor


def server_thread():
    global s

    while True:
        try:
            msg = s.recv(1024)
            msg = json.loads(msg.decode())

            if msg['type'] == MessageTypes.UPDATE_BALLS.value:
                data = json.loads(msg['data'])
                updateBalls(data)

            elif msg['type'] == MessageTypes.WINNER.value:
                print(msg['data'])
                s.close()
                screen.close()
                break

        except:
            pass


# Atualiza posição das bolas na tela
def updateBalls(ball_dict):
    global screen

    for i, value in enumerate(ball_dict.values()):
        ball = screen.ball_list[i]
        ball.circle_x, ball.circle_y = value[1], value[2]

        screen.update()


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Cria socket
host = socket.gethostname()                # Noma da máquina local
port = 4322  # Reserva uma porta para o serviço.

s.connect((host, port))
s.send(str.encode(input("Digite seu nome: ")))

# Recebe mensagens do servidor até iniciar o jogo
while True:
    msg = s.recv(1024)
    msg = json.loads(msg.decode())

    if msg['type'] == MessageTypes.INFORMATION.value:
        print(msg['data'])

    elif msg['type'] == MessageTypes.START.value:
        data = json.loads(msg['data'])
        startGame(data)
        break
