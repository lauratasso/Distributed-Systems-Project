import socket                                   # Import socket module
s = []                             # Create a socket object
host = '' #socket.gethostname()                     # Get local machine name
port = 4323 	                                   # Reserve a port for your service.
                            # Bind to the port
print ('esperando conexao')

c = []
addr = []
i=0
data=[]                                     # Now wait for client connections.
while i<4:
   s.append(socket.socket())
   s[i].bind((host, port+i))
   s[i].listen(5)
   aux, aux2 = s[i].accept()
   c.append(aux)
   addr.append(aux)
   data.append( c[i].recv(1024) )
   print (data[i], 'ENTROU NO JOGO! SUA COR EH')
# aqui cria a bolinha e retorna a cor da bolinha pro cliente 1
   x=0
   while x<i:
    c[x].send(' entrou no jogo! sua cor eh retorno da funcao que cria a bolinha')
    x=x+1
 # raw_input() vai ser substituido pela cor da bolinha
   i=i+1         
c.close()                                    # Close the connection

