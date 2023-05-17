import socket

# Configuração do endereço e porta do servidor
multicast_group = '224.0.0.1'  # Endereço de multicast
server_address = ('', 10000)  # Porta do servidor

# Criação do socket multicast
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Configuração do socket para uso de multicast
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, socket.inet_aton(multicast_group) + socket.inet_aton('0.0.0.0'))

# Bind do socket à porta do servidor
sock.bind(server_address)

# Loop principal do servidor
while True:
    print('Aguardando mensagem do cliente...')

    # Recebe a mensagem do cliente
    data, address = sock.recvfrom(1024)

    # Converte a mensagem recebida para string
    message = data.decode()

    # Inverte a string
    inverted_message = message[::-1]

    # Envia a mensagem invertida de volta para o cliente
    sock.sendto(inverted_message.encode(), address)

    print('Mensagem invertida enviada para o cliente:', inverted_message)
