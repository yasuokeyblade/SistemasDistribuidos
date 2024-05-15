import socket

def start_server():
    # Use o endereço IP da máquina do servidor
    server_ip = 'SEU_ENDERECO_IP_AQUI'
    server_port = 12345
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_ip, server_port))
    server_socket.listen(5)
    print(f"Servidor esperando por conexões em {server_ip}:{server_port}...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Conexão estabelecida com {addr}")

        while True:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"Mensagem recebida: {message}")
            client_socket.send("Mensagem recebida".encode('utf-8'))
        
        client_socket.close()
        print(f"Conexão com {addr} encerrada")

if __name__ == "__main__":
    start_server()
