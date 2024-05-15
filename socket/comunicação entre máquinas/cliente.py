import socket  # Importa a biblioteca de sockets, que permite a comunicação entre computadores em rede.

def send_message(message):
    # Define o endereço IP e a porta do servidor.
    server_ip = 'SEU_ENDERECO_IP_AQUI'
    server_port = 12345
    
    # Cria um objeto socket. AF_INET especifica que estamos usando IPv4.
    # SOCK_STREAM indica que estamos usando o protocolo TCP.
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Conecta o socket do cliente ao endereço IP e porta do servidor.
    client_socket.connect((server_ip, server_port))
    
    # Envia a mensagem ao servidor.
    client_socket.send(message.encode('utf-8'))
    
    # Recebe a resposta do servidor.
    response = client_socket.recv(1024).decode('utf-8')
    print(f"Resposta do servidor: {response}")
    
    # Fecha a conexão com o servidor.
    client_socket.close()

if __name__ == "__main__":
    # Solicita ao usuário que digite a mensagem a ser enviada.
    message = input("Digite a mensagem a ser enviada: ")
    # Envia a mensagem.
    send_message(message)
