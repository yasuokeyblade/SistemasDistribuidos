import socket

class LogicalClock:
    def __init__(self):
        self.time = 0

    def increment(self):
        self.time += 1

    def update(self, received_time):
        self.time = max(self.time, received_time) + 1

    def get_time(self):
        return self.time

def local_event(clock):
    clock.increment()
    print(f"Evento local no tempo {clock.get_time()}")

def send_message(clock, other_host, other_port):
    clock.increment()
    message = f"{clock.get_time()}"
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((other_host, other_port))
        s.sendall(message.encode('utf-8'))
    print(f"Enviando mensagem no tempo {clock.get_time()}")

if __name__ == "__main__":
    clock = LogicalClock()
    other_host = 'localhost'
    other_port = 12345  # Porta do servidor para onde enviar mensagens

    while True:
        action = input("Insira a ação (event/send/exit): ")
        if action == "event":
            local_event(clock)
        elif action == "send":
            send_message(clock, other_host, other_port)
        elif action == "exit":
            break
