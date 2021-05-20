from socket import *

server_port = 12000

server_socket = socket(AF_INET, SOCK_STREAM)

server_socket.bind(('', server_port))

server_socket.listen(1)

print('Server ON!')

while(True):
	connection_socket, addr = server_socket.accept()
	message = connection_socket.recv(2048)
	print('Mensagem Recebida: ', message)
	print('IP do cliente: ', addr[0])
	print('Porta do cliente: ', addr[1])
	modified_message = message.upper()
	connection_socket.send(modified_message)
	print('Mensagem Enviada: ', modified_message)
	connection_socket.close()

	print()
