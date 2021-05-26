from socket import *

server_name = 'localhost'
server_port = 12000

client_socket = socket(AF_INET, SOCK_STREAM)

client_socket.connect((server_name, server_port))

message = bytes(input('Insira a mensagem com letras minusculas: '), 'utf-8')

client_socket.send(message)

modified_message = client_socket.recv(2048)

print(modified_message)

client_socket.close()