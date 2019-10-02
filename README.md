# Projeto de Sistemas Distribuídos

## Projeto: 
Criar um servidor de jogo, estilo “Pong” (porém somente a bolinha), em tempo real, onde vários clientes poderão acessar e ver as bolinhas se chocando. Cada cliente tem uma bolinha e ganha o jogo o cliente cuja bolinha atingir um dos cantos primeiro.

## Funcionamento: 
### Preparação
Ao receber uma conexão, o servidor cria uma bolinha para o cliente, contendo cor única e posições aleatórias. 
O servidor aguarda que um número fixo N de clientes se conectem para iniciar o jogo. 

### Inicio do Jogo
Para dar inicio, o servidor faz brodcast das posições e cores de todas as bolinhas para todos os clientes, de modo que os clientes adicionem todas as bolinhas em suas telas. 

### O Jogo
A cada 0.08 segundos o servidor atualiza a posição das bolinhas e faz broadcast das novas posições aos clientes. 
Os clientes acompanham o movimento de todas as bolinhas, enquanto essas são constantemente atualizadas.
O jogo acaba assim que uma das bolinhas atinge um dos 4 cantos da tela, sendo o dono daquela bolinha o cliente ganhador. 

### Exemplo
Um exemplo do fluxo principal do jogo em um cenário com dois jogadores pode ser visto no diagrama à seguir: 

<p align="center">
  <img src="https://lh3.googleusercontent.com/1AF2T06uZawfN7Uxz83cOnk1BKKYlLVbAS7lyj3JkhT7qwOUV3bGJ7hSz2N35q60vMFUbh13Cp1fbac0BvLaKXCBQaa25DXetfVOzJKsWMkP-YyhCssH5kfQzFXHPlqEtH2rSSdpaEjzP2dJmZpq2J8kenwYdPJgeApR2OoWpO8pikbySkrNM5KjjbJKp_a-RpFGPhqk-6zRrpqIMvdpu92T_5xcW5SyPa6b_BhksAc3Gon5JKTwlGb1p82X_SQSffUtEC1XtOY3fG9afwWnis1_sf5Bu0bODuqRIDWoR3iW6DjAp2eiQTHVn15rPlTzLQeJVD_cX9M48UyCS7gQjo_RHNSK1k5e4MvGI_1c3vOEmwTLXfremnPx2NTUFQUfJvoJe77x6UBd-9CFGxnq-C_XnMfwiCUBB3BSa8cem3XPG3NNazkhdX0lvtQGAXXLi_XJbH5VRjgD2cEPkdP5DhSP77quWG1FbbcIEYLpZ3nXzbUTGeE-b3rgUuLF_fqREuFuDB0EtZ96MRp7VTvj50XoHUj3k6xd4QllCiuWYF-pJQZFbD2V5uFSiZo3cr6hkz5bC6OKmK4gYJK9S0ou4Nla3QptA2fpNbnOnva5fWW4pzkYIeeIfQKgRkU" width="500">
  <br>
  Exemplo de fluxo de mensagens trocadas entre servidor e clientes.
  <br>
</p>


## Implementação
A aplicação foi feita usando a linguagem Python 3 e a plataforam Pygame para a criação da interface do jogo. 
Para a comunicação entre o servidor e os clientes foi usado TCP/IP, por meio de sockets. 


## Intruções Para Funcionamento

Para rodar o projeto é necessário ter instalado:
- [**Python 3**](https://www.python.org/downloads/)
- [**Gerenciador de pacotes pip**](https://pip.pypa.io/en/stable/installing/)
- [**Pygame**](https://www.pygame.org/download.shtml)

Pelo pronpt de comando navege até a pasta *src*.

Para inciar o servidor, entre com o comando:
```
py server.py
```

Para inciar os clientes, em outros terminais, digite:
```
py client.py
```


Testes:

- Demonstração das funcionalidades: Mostrar que as funcionalidades foram implementadas com sucesso;
- Teste de concorrência: Mostrar que múltiplos usuários podem acessar a aplicação ao mesmo tempo;
- Teste de recuperação de falhas: Mostrar que se a aplicação falhar, não haverá nenhum estado inesperado quando voltar a funcionar.
