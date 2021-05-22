# para utilizar este código é necessário
# modificar as opcoes de seguranca da conta e
# habilitar o acesso de aplicativos menos seguros através do link:
# https://myaccount.google.com/intro/security

import smtplib
from email.mime.text import MIMEText

# conexão com os servidores do google
smtp_ssl_host = 'smtp.gmail.com'
smtp_ssl_port = 465
# username ou email para logar no servidor
username = 'xxxxxx@gmail.com'
password = 'xxxxxxx'

from_addr = 'xxxxxxx@gmail.com'
to_addrs = ['yyyyyyy@gmail.com']

# a biblioteca email possuí vários templates
# para diferentes formatos de mensagem
# neste caso usaremos MIMEText para enviar
# somente texto
message = MIMEText('Hello World')
message['subject'] = 'Hello'
message['from'] = from_addr
message['to'] = ', '.join(to_addrs)

# conectaremos de forma segura usando SSL
server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
# para interagir com um servidor externo precisaremos
# fazer login nele
server.login(username, password)
server.sendmail(from_addr, to_addrs, message.as_string())
server.quit()