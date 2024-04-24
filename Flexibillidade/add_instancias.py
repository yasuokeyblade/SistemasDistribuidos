import threading
import time

class ServicoPedido(threading.Thread):
    def run(self):
        while True:
            print("Processando pedido...")
            time.sleep(1)

# Função para criar uma nova instância do serviço de pedido
def adicionar_instancia():
    instancia = ServicoPedido()
    instancia.start()
    print("Nova instância de serviço de pedido adicionada.")

# Simulação de aumento na carga de trabalho
def aumentar_carga_trabalho():
    print("Aumentando carga de trabalho...")
    # Aqui poderiamos monitorar a carga real do sistema e decidir adicionar uma nova instância baseado em algum critério.

# Simulação: Iniciar com uma instância
servico_pedido = ServicoPedido()
servico_pedido.start()

# Simulação: Aumentar a carga de trabalho após 5 segundos
time.sleep(5)
aumentar_carga_trabalho()
adicionar_instancia()

# O sistema continuaria monitorando a carga de trabalho e adicionando instâncias conforme necessário.
