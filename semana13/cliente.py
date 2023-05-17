import socket

# Define o endereço do servidor e a porta
HOST = '127.0.0.1'
PORT = 12345

# Cria um socket TCP/IP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecta o socket ao endereço e porta
client_socket.connect((HOST, PORT))

# Envia uma mensagem de exemplo para o servidor
message = 'SEND_MESSAGE:alice:Hello, Alice!'
client_socket.sendall(message.encode('utf-8'))

# Recebe a resposta do servidor
response = client_socket.recv(1024).decode('utf-8')

# Processa a resposta do servidor
response_parts = response.split(':')
response_type = response_parts[0]
response_body = response_parts[1]

# Fecha o socket do cliente
client_socket.close()
