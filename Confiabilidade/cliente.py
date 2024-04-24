import Pyro4
import random
import time

if __name__ == "__main__":
    # Obter a referência do objeto remoto do serviço de pedido
    servico_pedido = Pyro4.Proxy("PYRO:servico_pedido@localhost:9093")

    while True:
        try:
            pedido = random.randint(1, 1000)
            resultado = servico_pedido.processar_pedido(pedido)
            print(resultado)
        except Pyro4.errors.CommunicationError:
            print("Erro: Não foi possível conectar ao servidor. Tente novamente mais tarde.")
        time.sleep(random.uniform(0.1, 0.5))
