import socket                                   # Import socket module

s = socket.socket()                             # Create a socket object
host = '' # socket.gethostname()                # Get local machine name
port = 4323                                    # Reserve a port for your service.

s.connect((host, port))
while True:

 s.send(raw_input())
 data = s.recv(1024)
 print (data)
 if data=='SAIR' :
  break
s.close()    
