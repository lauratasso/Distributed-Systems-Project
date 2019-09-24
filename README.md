# Projeto de Sistemas Distribuídos

Ideia Inicial: Criar um servidor de jogo, estilo “Pong” (porém somente a bolinha), em tempo real, onde vários clientes poderão acessar e ver as bolinhas se chocando.

Funcionamento: Cada cliente irá se conectar ao servidor, gerando assim uma bolinha para ele no jogo, com uma cor específica, e tal cliente irá acompanhar em tempo real o movimento da bolinha dele e de outros clientes, definido pelo servidor. O usuário poderá somente visualizar o jogo, não poderá modificá-lo.
    
Testes:

- Demonstração das funcionalidades: Mostrar que as funcionalidades foram implementadas com sucesso;
- Teste de concorrência: Mostrar que múltiplos usuários podem acessar a aplicação ao mesmo tempo;
- Teste de recuperação de falhas: Mostrar que se a aplicação falhar, não haverá nenhum estado inesperado quando voltar a funcionar.
