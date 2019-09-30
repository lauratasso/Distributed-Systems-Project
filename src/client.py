import socket
from threading import Thread
import json

from classes.screen import Screen
from classes.ball import Ball

# Thread dedicada para comunicação com o servidor


def server_thread():
    global s

    while True:
        data = s.recv(1024)
        try:
            data_balls = json.loads(data.decode())
            updateBalls(data_balls)
        except:
            pass

        if data == "SAIR":
            s.close()
            break

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

# Recebe lista de bolas do servidor e adiciona à tela
data = s.recv(1024)
screen = Screen()

data_balls = json.loads(data.decode())

for value in data_balls.values():
    ball = Ball(tuple(value[0]), value[1], value[2])
    screen.ball_list.append(ball)

# Inicializa thread do servidor
thread_conn = Thread(target=server_thread)
thread_conn.start()

# Inicializa tela
screen.run()
