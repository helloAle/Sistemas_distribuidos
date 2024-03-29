import socket

HOST = '127.0.0.1'  # Endereço IP do servidor
PORT = 65432        # Porta do servidor

# Definir o protocolo de comunicação
# O protocolo consiste em mensagens no formato "tipo|dados"
# O tipo pode ser "MSG" para mensagens de texto ou "ITEM" para informações de item
# Os dados podem ser uma mensagem de texto ou informações de item no formato "nome|quantidade"
def receive_message(s):
    data = s.recv(1024).decode()
    parts = data.split('|')
    return parts[0], parts[1]

def send_message(s, type, data):
    data = f"{type}|{data}".encode()
    s.sendall(data)

def handle_response(type, data):
    if type == 'MSG':
        print(f'Mensagem ecoada: {data}')
    else:
        print(f'Tipo de mensagem inválido: {type}')

def execute_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        # Adicionar um item
        send_message(s, 'ADD', 'Arroz|2')
        # Receber a mensagem de resposta
        type, data = receive_message(s)
        handle_response(type, data)
        # Remover um item
        send_message(s, 'REMOVE', 'Arroz')
        # Receber a mensagem de resposta
        type, data = receive_message(s)
        handle_response(type, data)
        # Atualizar um item
        send_message(s, 'UPDATE', 'Feijão|3')
        # Receber a mensagem de resposta
        type, data = receive_message(s)
        handle_response(type, data)
        # Buscar um item
        send_message(s, 'GET', 'Feijão')
        # Receber a mensagem de resposta
        type, data = receive_message(s)
        handle_response(type, data)

execute_client()
