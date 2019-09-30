import json
INTERVAL = 0.08

# Classe para guardar o estado do servidor


class ServerState(object):

    # Construtor da classe
    def __init__(self):

        self.clients = {}
        self.nro_clients = 0
        self.next_client = None
        self.client_balls = []

    # Adiciona novo cliente conectado ao servidor
    def add_client(self, addr, name, socket):

        self.clients[addr] = (name, socket)
        self.nro_clients += 1

    # Retorna cliente com enredeço indicado
    def get_client_socket(self, addr):

        return self.clients[addr]

    # Retorna posição de todas as bolas. Se update for verdadeiro, atualiza as posições antes de retorna-las
    def get_balls_pos(self, update):

        json_dict = {}
        for i, (data, _) in enumerate(self.clients.values()):

            if(update):
                x, y, sx, sy = self.update_ball_pos(self.client_balls[i][1], self.client_balls[i]
                                                    [2], self.client_balls[i][3], self.client_balls[i][4])

                self.client_balls[i][1], self.client_balls[i][2] = x, y
                self.client_balls[i][3], self.client_balls[i][4] = sx, sy
            json_dict[data.decode()] = self.client_balls[i]

        return json.dumps(json_dict)

    # Atualiza posição das bolas
    def update_ball_pos(self, circle_x, circle_y, speed_x, speed_y):

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
