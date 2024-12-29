class Singleton(object):
    _instance = None  # Keep instance reference
    # why do this???? If do this, the if state follow is always false, right?
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls, *args, **kwargs)
            print("creating")
        return cls._instance

a = Singleton()
b = Singleton()
print(a is b)
 
# https://stackoverflow.com/questions/50670103/python-singleton-code
# https://medium.com/geekculture/python-five-ways-to-write-singleton-b6afbed65680

"""
__new__também é um método de classe que substitui o __init__método (você tem controle sobre o objeto que é criado neste nível)

_instance é um atributo de classe, não um atributo de instância. Portanto, está visível/disponível no __new__método antes que uma instância seja criada.

Então, na primeira vez, o cls._instanceargumento é None, então __new__cria a instância e armazena o resultado no _instance atributo de classe cls(que é sua Singletonclasse)

Não é None a segunda vez porque a referência da instância foi armazenada , então ela retorna o mesmo self._instanceobjeto. No processo, object.__new__é chamado apenas uma vez durante o tempo de vida da classe.

Isso segue o padrão de design do singleton : crie uma vez, retorne o mesmo objeto todas as vezes.

"""