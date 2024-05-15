import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(5)
    print("Servidor esperando por conexões...")

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
