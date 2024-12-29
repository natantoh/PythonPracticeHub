# Padrão Pyhon Letra maiscula inicial para Classe
# Métodos acessiveis são pulbicos, não contém o __. O __ são métodos privados.

class Pessoa:
    def __init__(self,nome_da_pessoa,idade_da_pessoa,cpf_da_pessoa):
        self.nome = nome_da_pessoa
        self.idade = idade_da_pessoa
        self.__cpf = cpf_da_pessoa # Queremos que o CPF não seja acessível, por isso a convensão do python é utilizar dois underlines depois do self, assim: self.__cpf
        #print(self.__cpf) # imprimi o CPF quando está dentro de __init__ e também imprimi a partir de um método printar cpf como mostrado abaixo como exemplo,  mas o __cpf não é acessível fora da classe.
    
    def printar_cpf(self):
        print(self.__cpf) # Agora 

    def correr(self):
        print("Estou correndo")
    
    def beber_cerveja(self, bebida):
        if bebida == "cerveja":
            numero_do_documento = self.__apresentar_documento()
            if numero_do_documento == "246548":
                print("Pode Beber, cliente VIP")
                # print(f"Pode Beber, seu documento eh:{numero_do_documento}") Não imprimirá pois o método é privado.
            
    def __apresentar_documento(self):
        print(self.__cpf)

pessoa1 = Pessoa("Joao","20","241850999996548")

print(pessoa1.nome)

# Em resumo: 
#print(pessoa1.__cpf) # Não consegue imprimir o cpf acessando o atributo cpf. Apenas como método como abaixo.
#pessoa1.printar_cpf() # Imprimi o CPF a partir da classe
#pessoa1.__apresentar_documento() # Não consegue imprimir o CPF pois o método é privado. Tem que retirar o __ do método.
pessoa1.beber_cerveja("cerveja") 




    
    
 