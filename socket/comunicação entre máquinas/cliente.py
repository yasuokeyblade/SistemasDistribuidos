import socket

def send_message(message):
    # Use o endereço IP da máquina do servidor
    server_ip = 'SEU_ENDERECO_IP_AQUI'
    server_port = 12345
    
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))
    
    client_socket.send(message.encode('utf-8'))
    response = client_socket.recv(1024).decode('utf-8')
    print(f"Resposta do servidor: {response}")
    
    client_socket.close()

if __name__ == "__main__":
    message = input("Digite a mensagem a ser enviada: ")
    send_message(message)
