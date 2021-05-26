from socket import *
import time
import numpy as np

server_name = 'localhost'
server_port = 12000

#criacao de um objeto socket. parametros = (familia de ip (ipv4), definicao do protocolo UDP)
client_socket = socket(AF_INET, SOCK_DGRAM)

#input de dados
ping_message = b'ping'

rtt_list = []

for i in range(10):
	ti = time.time()
	#envia mensagem para o servidor
	client_socket.sendto(ping_message, (server_name, server_port))
	#recebe resposta do servidor
	pong_message, server_address = client_socket.recvfrom(2048)
	tf = time.time()
	rtt = tf-ti
	print(i, ' - RTT: ', rtt)
	rtt_list.append(rtt)

rtt_array = np.asarray(rtt_list)
print()
print('RTT mínimo: ', rtt_array.min())
print('RTT máximo: ', rtt_array.max())
print('RTT médio: ', rtt_array.mean())

client_socket.close()