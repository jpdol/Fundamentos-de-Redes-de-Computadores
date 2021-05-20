from socket import *

server_name = 'localhost'
server_port = 12000

#criacao de um objeto socket. parametros = (familia de ip (ipv4), definicao do protocolo UDP)
client_socket = socket(AF_INET, SOCK_DGRAM)

#input de dados
message = input('Insira a mensagem com letras minusculas: ')

client_socket.sendto(bytes(message, 'utf-8'), (server_name, server_port))

#recebe resposta do servidor
modfied_message, server_address = client_socket.recvfrom(2048)

print(modfied_message)

client_socket.close()