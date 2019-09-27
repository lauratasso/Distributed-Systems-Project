import socket

NRO_CLIENTS = 4

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a socket object
host = "0.0.0.0"  # socket.gethostname()                     # Get local machine name
port = 4324  # Reserve a port for your service.
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

    def add_client(self, addr, name, socket):

        self.clients[addr] = (name, socket)
        self.nro_clients += 1

    def get_client_socket(self, addr):

        return self.clients[addr]


state = ServerState()

# Esperando 4 clientes se conectarem
for _ in range(NRO_CLIENTS):

    conn, addr = socket.accept()  # Aceita conexao, retorna tupla socket, endereco
    data = conn.recv(1024)
    state.add_client(addr, data, conn)  # Adiciona o cliente no estado do servidor

    print(data, "ENTROU NO JOGO! SUA COR EH")

    state.next_client = (data, conn) if state.next_client is None else state.next_client
    # # aqui cria a bolinha e retorna a cor da bolinha pro cliente 1
    # x = 0
    # while x < i:
    #     c[x].send(" entrou no jogo! sua cor eh retorno da funcao que cria a bolinha")
    #     x = x + 1
    # # raw_input() vai ser substituido pela cor da bolinha
    # i = i + 1

# Avisando aos clientes que o jogo começou
for _, cl_socket in state.clients.values():

    curr_name, curr_conn = state.next_client
    cl_socket.send(
        str.encode(
            f"O jogo começou. \
            {'Eh a sua vez' if curr_conn == cl_socket else 'E a vez de ' + str(curr_name) }"
        )
    )

while True:
    for _, cl_socket in state.clients.values():
        cl_socket.send(b"Ola tudo bem?")
