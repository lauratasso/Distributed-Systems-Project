import socket
import random
import time
import json

from classes.server import ServerState
from classes.message import Message
from utils.color import colors
from utils.message_type import MessageTypes

NRO_CLIENTS = 2
INTERVAL = 0.08

# Cria socket
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "0.0.0.0"  # socket.gethostname()                     # Get local machine name
port = 4322  # Reserve a port for your service.

socket.bind((host, port))  # Escutando na pota 4323
socket.listen(NRO_CLIENTS)  # Conexão com no máximo N clients
print(f"Esperando conexões. É necessário {NRO_CLIENTS} para começar o jogo.")


def random_ball(color):
    # cria posição randomica para bola
    coord_x = random.uniform(10, 630)
    coord_y = random.uniform(10, 470)

    speed_x = 250.
    speed_y = 250.

    # retorna lista com parametros necessários para manipulação da bola
    return [color, coord_x, coord_y, speed_x, speed_y]


state = ServerState()

# Esperando N clientes se conectarem
for i in range(NRO_CLIENTS):

    conn, addr = socket.accept()  # Aceita conexao, retorna tupla socket, endereco
    data = conn.recv(1024)

    # Adiciona o cliente no estado do servidor
    state.add_client(addr, data, conn)
    color = colors[i]   # Pega cor [i] para a bola do cliente.

    # Informa jogador sua cor e se faltam clientes para o inicio do jogo
    data = f"\n{data.decode()} entrou no jogo. Sua cor é: {color[2]}{color[0]}"+'\033[0;0m'

    if (NRO_CLIENTS - 1 - i > 0):
        data += f"\nFaltam {NRO_CLIENTS - i -1} jogadores para iniciar o jogo. Aguarde."
    else:
        data += "\nO jogo começará em breve."

    # Envia dados de cor e inicio do jogo para o cliente
    msg = Message(MessageTypes.INFORMATION.value, data).toJSON()
    (_, cl_socket) = state.clients[addr]
    cl_socket.send(str.encode(msg))

    state.next_client = (
        data, conn) if state.next_client is None else state.next_client

    ball = random_ball(color[1])
    state.client_balls.append(ball)

# Avisando aos clientes que o jogo começou
for i, (_, cl_socket) in enumerate(state.clients.values()):
    curr_name, curr_conn = state.next_client
    msg = Message(MessageTypes.START.value,
                  state.get_balls_pos(False)).toJSON()

    cl_socket.send(
        str.encode(
            msg
        )
    )

# Atualizando posição das bolas e mandando para os clientes
time.sleep(2)
while True:
    time.sleep(INTERVAL)

    # verifica se há ganhador
    winner = state.check_winner()

    if (winner):
        data = f"\n{winner.upper().decode()} GANHOU O JOGO!!"
        msg = Message(MessageTypes.WINNER.value, data).toJSON()

    else:
        result = state.get_balls_pos(True)
        msg = Message(MessageTypes.UPDATE_BALLS.value, result).toJSON()

    for _, cl_socket in state.clients.values():
        cl_socket.send(
            str.encode(
                msg
            )
        )

    if winner:
        break
