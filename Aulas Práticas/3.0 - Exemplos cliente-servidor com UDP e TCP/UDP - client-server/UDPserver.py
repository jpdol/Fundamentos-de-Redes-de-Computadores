from socket import *

server_port = 12000

server_socket = socket(AF_INET, SOCK_DGRAM)

server_socket.bind(('', server_port))

print('Servidor on!')

while (True):
	message, client_address = server_socket.recvfrom(2048)
	print('Mensagem Recebida: ', message)
	print('IP do cliente: ', client_address[0])
	print('Porta do cliente: ', client_address[1])
	modified_message = message.upper()
	print('Nova Mensagem: ', modified_message)
	server_socket.sendto(modified_message, client_address)
	print()