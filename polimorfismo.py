# Exemplo Básico de polimorfismo

class PessoaA:
    def se_apresentar(self):  # PessoaA tem o método se_apresentar.
        print("Ola, eu sou a pessoaA")

class PessoaB(PessoaA):
    def __init__(self):
        super().__init__()

    def se_apresentar(self):
        print("Estou alterando esse metodo, poliformismo.")

class PessoaC(PessoaB):
    def __init__(self):
        super().__init__()


pessoa1 = PessoaA()
pessoa1.se_apresentar()

pessoa2 = PessoaB()
pessoa2.se_apresentar()

pessoa3 = PessoaC()
pessoa3.se_apresentar()

pessoa1 = PessoaA()
pessoa1.se_apresentar()


