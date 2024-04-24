import threading  # Biblioteca para suportar programação concorrente em Python, permitindo a execução simultânea de várias threads para realizar tarefas em paralelo.
import time  # Biblioteca que fornece funções relacionadas ao tempo, como medir o tempo decorrido, pausar a execução do programa etc.
import Pyro4  # Pyro (Python Remote Objects) é um framework para programação distribuída em Python. Ele facilita a comunicação entre objetos em diferentes processos ou máquinas através de chamadas de procedimento remoto (RPC).
import random  # Biblioteca para geração de números aleatórios e outras operações relacionadas à aleatoriedade.
import sys  # Biblioteca que fornece acesso a algumas variáveis e funções mantidas ou usadas pelo interpretador Python, como argumentos de linha de comando, manipulação de exceções e finalização do programa.


# Simulação de vários clientes fazendo solicitações
class Cliente(threading.Thread):
    def __init__(self, nome):
        super().__init__()
        self.nome = nome
        self.servico = None

    def run(self):
        try:
            self.servico = Pyro4.Proxy("PYRO:servico_pedido@localhost:9093")
            print("Cliente", self.nome, "conectado ao servidor")
        except Pyro4.errors.CommunicationError:
            print("Erro: Não foi possível conectar ao servidor. O cliente", self.nome, "será encerrado.")
            sys.exit(1)

        while True:
            try:
                print("Cliente", self.nome, "fazendo uma solicitação")
                self.servico.processar_pedido(self.nome)
                time.sleep(2)
            except Pyro4.errors.CommunicationError:
                print("Erro: Não foi possível comunicar com o servidor. O cliente", self.nome, "será encerrado.")
                sys.exit(1)

if __name__ == "__main__":
    # Inicia vários clientes
    for i in range(3):
        nome_cliente = "Cliente_" + str(i+1)
        cliente = Cliente(nome_cliente)
        cliente.start()
