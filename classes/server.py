import socket
import random
import time
import json

NRO_CLIENTS = 2
INTERVAL = 0.08

# Create a socket object
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "0.0.0.0"  # socket.gethostname()                     # Get local machine name
port = 4322  # Reserve a port for your service.
# Bind to the port
socket.bind((host, port))  # Escutando na pota 4323
socket.listen(NRO_CLIENTS)  # Conexão com no máximo 4 clients
print("Esperando conexao")


# Classe para guardar o estado do servidor
class ServerState(object):
    def __init__(self):

        self.clients = {}
        self.nro_clients = 0
        self.next_client = None
        self.client_balls = []

    def add_client(self, addr, name, socket):

        self.clients[addr] = (name, socket)
        self.nro_clients += 1

    def get_client_socket(self, addr):

        return self.clients[addr]

    def get_balls_pos(self, update):

        json_dict = {}
        for i, (data, _) in enumerate(self.clients.values()):

            if(update):
                x, y, sx, sy = move(self.client_balls[i][1], self.client_balls[i]
                                    [2], self.client_balls[i][3], self.client_balls[i][4])

                self.client_balls[i][1], self.client_balls[i][2] = x, y
                self.client_balls[i][3], self.client_balls[i][4] = sx, sy
            json_dict[data.decode()] = self.client_balls[i]

        return json.dumps(json_dict)


def random_ball():
    # creating randomly the position of the ball
    coord_x = random.uniform(10, 630)
    coord_y = random.uniform(10, 470)

    # choosing randomly the color of the ball
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    if r < 40 and g < 40 and b < 40:
        r = 45
        g = 45
        b = 45

    speed_x = 250.
    speed_y = 250.

    return [(r, g, b), coord_x, coord_y, speed_x, speed_y]


def move(circle_x, circle_y, speed_x, speed_y):

    # time_passed = clock.tick(30)
    # time_sec = time_passed / 1000.0

    time_sec = INTERVAL

    circle_x += speed_x * time_sec
    circle_y += speed_y * time_sec

    if circle_x <= 10.:
        if circle_y >= 7.5 and circle_y <= 470:
            circle_x = 20.
            speed_x = -speed_x
    if circle_x >= 630.:
        if circle_y >= 7.5 and circle_y <= 470:
            circle_x = 605.
            speed_x = -speed_x
    if circle_y <= 10.:
        speed_y = -speed_y
        circle_y = 10.
    elif circle_y >= 457.5:
        speed_y = -speed_y
        circle_y = 457.5

    return circle_x, circle_y, speed_x, speed_y


state = ServerState()

# Esperando 4 clientes se conectarem
for _ in range(NRO_CLIENTS):

    conn, addr = socket.accept()  # Aceita conexao, retorna tupla socket, endereco
    data = conn.recv(1024)
    # Adiciona o cliente no estado do servidor
    state.add_client(addr, data, conn)

    print(data, "ENTROU NO JOGO! SUA COR EH")

    state.next_client = (
        data, conn) if state.next_client is None else state.next_client

    ball = random_ball()
    state.client_balls.append(ball)
    # # aqui cria a bolinha e retorna a cor da bolinha pro cliente 1
    # x = 0
    # while x < i:
    #     c[x].send(" entrou no jogo! sua cor eh retorno da funcao que cria a bolinha")
    #     x = x + 1
    # # raw_input() vai ser substituido pela cor da bolinha
    # i = i + 1

# Avisando aos clientes que o jogo começou
for i, (_, cl_socket) in enumerate(state.clients.values()):

    curr_name, curr_conn = state.next_client
    cl_socket.send(
        str.encode(
            f"{state.get_balls_pos(False)}"
        )
    )

time.sleep(2)
while True:
    time.sleep(INTERVAL)
    result = state.get_balls_pos(True)
    for _, cl_socket in state.clients.values():
        cl_socket.send(result.encode())
