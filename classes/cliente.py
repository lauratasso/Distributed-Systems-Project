import socket  # Import socket module

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a socket object
host = "0.0.0.0"  # socket.gethostname()                # Get local machine name
port = 4324  # Reserve a port for your service.

s.connect((host, port))
s.send(str.encode(input("Digie seu nome: ")))
data = s.recv(1024)


while True:
    data = s.recv(1024)
    s.send(str.encode(input("Sua ação: ")))
    data = s.recv(1024)
    print(data)
    if data == "SAIR":
        break

s.close()
