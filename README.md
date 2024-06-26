[![N|Solid](https://universidadedevassouras.edu.br/wp-content/uploads/2022/03/campus_marica.png)](https://universidadedevassouras.edu.br/campus-marica/)

# Engenharia de Software
### Leandro Loffeu Pereira Costa - mat. 202212089
### Banco de dados não relacionais - 5º Período
### Professor: Fabicio


# chat-redis


Este tutorial fornecerá um passo a passo sobre como instalar e começar a usar o Redis no Windows, utilizando o Subsistema Windows para Linux (WSL2), uma vez que o Redis não possui uma versão oficial para Windows.
link: https://medium.com/@nelson.miranda_40644/tutorial-como-instalar-e-usar-o-redis-no-windows-0458407bead8

Instalar bibliotecas:

python-redis: pip install python-redis

Instale redis: pip install redis

Importe redis

![image](https://github.com/leandroloffeu/ChatRedis/assets/112645165/84794aa9-9307-455d-9376-480107b2dbfe)



Criar uma instância:

![image](https://github.com/leandroloffeu/ChatRedis/assets/112645165/26694f11-6b29-47b1-8668-20cec4023bc4)



criar as operações do Redis no endpoint WebSocket:


![image](https://github.com/leandroloffeu/ChatRedis/assets/112645165/8ad5b3fb-ae2b-4add-a2a4-1b0a3526911d)



Instalar a extensão Redis no VS Code:

Procure por "Redis" e instale a extensão de Dunn 
Conecte-se ao seu servidor Redis dentro da extensão
Abra a visualização Redis
Clique no botão “+” e insira os detalhes de conexão do seu servidor Redis (host, porta, senha, se aplicável

![image](https://github.com/leandroloffeu/chata-redis/assets/112645165/36a0e249-8904-4f09-82d5-14713a1a7d9f)


Iniciar o Servidor Redis: sudo service redis-server start

Verificar a Instalação: redis-cli

No prompt do Redis, digite ping. Se receber “PONG” como resposta, o Redis está funcionando corretamente.



Comando EXISTS: verifica se uma chave específica existe no Redis. Ele retorna 1 se a chave existir e 0 caso contrário.

redis-cli> EXISTS key_name

Comando KEYS: retorna uma lista com todas as chaves presentes no banco de dados Redis.

redis-cli> KEYS *

Comando DB SIZE: retorna o número total de chaves presentes no banco de dados Redis

redis-cli> DBSIZE




