from socket import *

# socket_host e socket_port 
SERVER_HOST = ''
SERVER_PORT = 1234

# criar socket
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))

server_socket.listen(1)

print('Server ON!')

while (True):
	# esperar por requisicao de clientes
	client_connection, client_address = server_socket.accept()

	# receber requisicao do cliente
	request = client_connection.recv(2048).decode()
	print(request)

	# parse HTTP headers
	headers = request.split('\n')
	filename = headers[0].split()[1]

	if filename == '/favicon.ico' or filename == '/':
		filename = '/index.html'

	# buscar conteudos
	try:
		file = open('htdocs' + filename)
		content = file.read()
		file.close()
		#criar mensagem de resposta para o clinte
		response = 'HTTP/1.0 200 OK\n\n' + content
	except FileNotFoundError:
		file = open('htdocs/404.html')
		content = file.read()
		file.close()
		response = 'HTTP/1.0 404 NOT FOUND\n\n' + content

	# enviar HTTP response
	client_connection.sendall(response.encode())
	client_connection.close()

server_socket.close()