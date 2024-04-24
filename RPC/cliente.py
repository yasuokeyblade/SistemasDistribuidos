import Pyro4

# Cria um proxy para se conectar ao servidor Pyro
def main():
    calculadora = Pyro4.Proxy("PYRO:obj_369e8b0f96954353a3b166bc579639db@localhost:53649")  # Substitua 'obj_123456' pelo URI do servidor
    resultado = calculadora.somar(85, 3)
    print("A soma é:", resultado)

if __name__ == "__main__":
    main()
