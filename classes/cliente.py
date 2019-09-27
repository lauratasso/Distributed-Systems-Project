import socket  # Import socket module
from pong import Tela
from ball import Ball
import random

def random_ball():
	#creating randomly the position of the ball
	coord_x = random.uniform(10,630)
	coord_y = random.uniform(10,470)

	#choosing randomly the color of the ball
	r = random.randint(0,255)
	g = random.randint(0,255)
	b = random.randint(0,255)

	if r < 25 and g < 25 and b < 25:
		r = 30
		g = 30
		b = 30

	return Ball((r,g,b), coord_x, coord_y)



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a socket object
host = "0.0.0.0"  # socket.gethostname()                # Get local machine name
port = 4322  # Reserve a port for your service.

s.connect((host, port))
s.send(str.encode(input("Digite seu nome: ")))
data = s.recv(1024) 
tela = Tela()

tela.ball_list.append(random_ball())
tela.run()

while True:
    data = s.recv(1024)
    #s.send(str.encode(input("Sua ação: ")))
    #data = s.recv(1024)
    print(data)
    if data == "SAIR":
        break

s.close()
