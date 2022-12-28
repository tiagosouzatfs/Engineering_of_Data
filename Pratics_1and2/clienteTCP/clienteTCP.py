# UNIVERSIDADE FEDERAL DO RIO GRANDE DO NORTE
# DEPARTAMENTO DE ENGENHARIA DE COMPUTACAO E AUTOMACAO
#
# AUTOR: PROF. CARLOS M D VIEGAS (viegas 'at' dca.ufrn.br)
#

# importacao das bibliotecas
from socket import *

# definicao das variaveis (rede do docker e do docker-compose são diferentes, então o ip muda, se quiser padronizar isso é criar uma rede e definir os ips)
serverName = '10.0.0.10' # ip do servidor criação rede interna com docker-compose
#serverName = '172.24.0.2' # ip do servidor (nesse caso vc dá um docker inspect no container do servidorTCP para pegar o ip dele) usando a rede docker-compose
#serverName = '172.17.0.2' # ip do servidor (nesse caso vc dá um docker inspect no container do servidorTCP para pegar o ip dele) usando a rede docker
serverPort = 30000 # porta a se conectar
clientSocket = socket(AF_INET,SOCK_STREAM) # criacao do socket TCP
clientSocket.connect((serverName, serverPort)) # conecta o socket ao servidor

print ('Cliente em execucao...\nEnviando mensagem para o servidor')
sentence = gethostname()
clientSocket.send(sentence.encode('utf-8')) # envia o texto para o servidor
clientSocket.close() # encerramento o socket do cliente
