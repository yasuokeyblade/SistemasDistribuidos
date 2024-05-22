import socket
import threading

class LogicalClock:
    def __init__(self):
        self.time = 0

    def increment(self):
        self.time += 1

    def update(self, received_time):
        self.time = max(self.time, received_time) + 1

    def get_time(self):
        return self.time

def receive_message(clock, conn):
    data = conn.recv(1024)
    received_time = int(data.decode('utf-8'))
    clock.update(received_time)
    print(f"Mensagem recebida no tempo {clock.get_time()}")

def start_server(host, port, clock):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f"Servidor ouvindo em {host}:{port}")
        while True:
            conn, addr = s.accept()
            with conn:
                print(f"Conexão estabelecida com {addr}")
                receive_message(clock, conn)

if __name__ == "__main__":
    host = 'localhost'
    port = 12345  # Defina a porta do servidor aqui
    clock = LogicalClock()
    start_server(host, port, clock)
