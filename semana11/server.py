import socket

def main():
    # Configuração do servidor
    host = '127.0.0.1'  # Endereço IP do servidor
    port = 8000  # Porta de comunicação

    # Criação do socket do servidor
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print('Servidor pronto para receber conexões.')

    while True:
        # Aguarda a conexão do cliente
        client_socket, addr = server_socket.accept()
        print('Cliente conectado:', addr)

        # Recebe a mensagem do cliente
        message = client_socket.recv(1024).decode()
        print('Mensagem recebida do cliente:', message)

        # Envia uma resposta ao cliente
        response = 'Mensagem recebida com sucesso!'
        client_socket.send(response.encode())

        # Fecha a conexão com o cliente
        client_socket.close()

if __name__ == '__main__':
    main()
