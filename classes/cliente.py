import socket  # Import socket module
from pong import Tela
from ball import Ball
import random
from threading import Thread
import json


def random_ball():
    # creating randomly the position of the ball
    coord_x = random.uniform(10, 630)
    coord_y = random.uniform(10, 470)

    # choosing randomly the color of the ball
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    if r < 25 and g < 25 and b < 25:
        r = 30
        g = 30
        b = 30

    return Ball((r, g, b), coord_x, coord_y)


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


def updateBalls(ball_dict):
    global tela

    for i, value in enumerate(ball_dict.values()):
        ball = tela.ball_list[i]
        ball.circle_x, ball.circle_y = value[1], value[2]

        tela.update()


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a socket object
host = socket.gethostname()                # Get local machine name
port = 4322  # Reserve a port for your service.

s.connect((host, port))
s.send(str.encode(input("Digite seu nome: ")))
data = s.recv(1024)
tela = Tela()

data_balls = json.loads(data.decode())

for value in data_balls.values():
    ball = Ball(tuple(value[0]), value[1], value[2])
    tela.ball_list.append(ball)

thread_conn = Thread(target=server_thread)
thread_conn.start()

tela.run()


# print("OI")

# while True:
#     data = s.recv(1024)
#     #s.send(str.encode(input("Sua ação: ")))
#     #data = s.recv(1024)
#     print(data)
#     if data == "SAIR":
#         break
