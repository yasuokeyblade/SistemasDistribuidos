import socket  # Importa a biblioteca de sockets, que permite a comunicação entre computadores em rede.

def start_server():
    # Define o endereço IP e a porta do servidor.
    server_ip = 'SEU_ENDERECO_IP_AQUI'
    server_port = 12345
    
    # Cria um objeto socket. AF_INET especifica que estamos usando IPv4.
    # SOCK_STREAM indica que estamos usando o protocolo TCP.
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Associa o socket ao endereço IP e porta especificados.
    server_socket.bind((server_ip, server_port))
    
    # Coloca o servidor em modo de escuta, com um limite de 5 conexões pendentes.
    server_socket.listen(5)
    print(f"Servidor esperando por conexões em {server_ip}:{server_port}...")

    while True:
        # Aceita uma conexão do cliente.
        client_socket, addr = server_socket.accept()
        print(f"Conexão estabelecida com {addr}")

        while True:
            # Recebe a mensagem do cliente. O tamanho máximo da mensagem é 1024 bytes.
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                # Se não houver mensagem (cliente desconectou), sai do loop interno.
                break
            print(f"Mensagem recebida: {message}")
            # Envia uma resposta ao cliente.
            client_socket.send("Mensagem recebida".encode('utf-8'))
        
        # Fecha a conexão com o cliente.
        client_socket.close()
        print(f"Conexão com {addr} encerrada")

if __name__ == "__main__":
    start_server()  # Inicia o servidor.
