import socket

def main():
    # Configuração do cliente
    host = '127.0.0.1'  # Endereço IP do servidor
    port = 8000  # Porta de comunicação

    # Criação do socket do cliente
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    # Solicita que o usuário digite uma mensagem
    message = input('Digite uma mensagem: ')

    # Envia a mensagem para o servidor
    client_socket.send(message.encode())

    # Recebe a resposta do servidor
    response = client_socket.recv(1024).decode()
    print('Resposta do servidor:', response)

    # Fecha a conexão com o servidor
    client_socket.close()

if __name__ == '__main__':
    main()
