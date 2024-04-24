import Pyro4

# Definir uma classe para o serviço remoto
@Pyro4.expose
class CalculadoraRemota:
    def somar(self, a, b):
        return a + b

# Iniciar o servidor Pyro
def main():
    daemon = Pyro4.Daemon()  # Cria um daemon para o servidor
    uri = daemon.register(CalculadoraRemota)  # Registra a classe CalculadoraRemota com o daemon
    print("URI do servidor:", uri)
    daemon.requestLoop()  # Inicia o loop do servidor para esperar por chamadas remotas

if __name__ == "__main__":
    main()
