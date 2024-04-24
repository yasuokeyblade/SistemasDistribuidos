import threading
import time
import Pyro4

# Classe do serviço de pedido
@Pyro4.expose
class ServicoPedido(threading.Thread):
    def processar_pedido(self, nome_cliente):
        print("Processando pedido de", nome_cliente, "no servidor", threading.current_thread().name)
        time.sleep(1)

# Iniciar servidor Pyro
def iniciar_servidor():
    # O daemon é responsável por gerenciar a comunicação entre os clientes e os objetos remotos.
    daemon = Pyro4.Daemon(port=9093)
    # Defina um ID de objeto único para garantir consistência na URI
    objectId = "servico_pedido"
    uri = daemon.register(ServicoPedido, objectId)
    print("URI do servidor:", uri)
    daemon.requestLoop()

if __name__ == "__main__":
    iniciar_servidor()

