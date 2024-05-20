# chat-redis


Este tutorial fornecerá um passo a passo sobre como instalar e começar a usar o Redis no Windows, utilizando o Subsistema Windows para Linux (WSL2), uma vez que o Redis não possui uma versão oficial para Windows.
link: https://medium.com/@nelson.miranda_40644/tutorial-como-instalar-e-usar-o-redis-no-windows-0458407bead8

Instalar bibliotecas:

python-redis: pip install python-redis

Instale redis: pip install redis

Importe redis

![image](https://github.com/leandroloffeu/chata-redis/assets/112645165/2c6778fb-8107-41e9-9239-da7d72cb6d20)

Criar uma instância:

![image](https://github.com/leandroloffeu/chata-redis/assets/112645165/45ea00ed-ebd2-4651-93d1-4bbfca1477e8)


criar as operações do Redis no endpoint WebSocket:

![image](https://github.com/leandroloffeu/chata-redis/assets/112645165/bc0cfa80-f9bb-4860-a634-69ac875fbc16)


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




