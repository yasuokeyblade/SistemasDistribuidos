import Pyro4
import threading
import time
import random

# Classe do serviço de pedido
@Pyro4.expose
class ServicoPedido:
    def __init__(self):
        self.pedidos_processados = 0
        self.funcionando = True

    def processar_pedido(self, pedido):
        # Verificar se o serviço está funcionando
        if not self.funcionando:
            return "Serviço indisponível no momento. Tente novamente mais tarde."

        # Simular processamento do pedido
        time.sleep(random.uniform(0.5, 1.5))
        self.pedidos_processados += 1
        print("Pedido processado:", pedido)
        return "Pedido processado com sucesso"

    def simular_falhas(self):
        while True:
            # Simular falhas ocasionalmente
            if random.random() < 0.1:
                print("Simulando uma falha...")
                self.funcionando = False
                time.sleep(random.uniform(1, 3))
                print("Reiniciando o serviço...")
                self.funcionando = True
            time.sleep(1)

if __name__ == "__main__":
    # Iniciar o serviço de pedido
    servico_pedido = ServicoPedido()

    # Registrar o objeto do serviço de pedido no Pyro
    daemon = Pyro4.Daemon(port=9093)
    # Defina um ID de objeto único para garantir consistência na URI
    objectId = "servico_pedido"
    uri = daemon.register(ServicoPedido, objectId)
    print("URI do servidor:", uri)

    # Iniciar o loop do daemon
    daemon_thread = threading.Thread(target=daemon.requestLoop)
    daemon_thread.start()

    # Thread para simular falhas
    thread_falhas = threading.Thread(target=servico_pedido.simular_falhas)
    thread_falhas.start()
