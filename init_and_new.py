"""
Segundo a definição abaixo:

Use o __new__ quando você precisar controlar a criação de uma nova instancia da classe. Use o __init__ quando você precisar controlar a inicialização de uma nova instancia.

O __new__ é o primeiro passo da criação de uma instancia. Ele é chamado primeiro, e é responsavel por retornar uma nova instancia da sua classe. Em contraste, o __init__ não retorna nada, ele é apenas responsável pela inicialização da instancia após a classe ser criada.

Em geral, você não deveria sobrepor o __new__ ao menos que seja uma subclasse, um tipo imutável como str, int, unicode ou tuple.

Ou seja, voce pode usar o __new__ para ter um controle da criação da instancia da classe e apos ele usar o __init__ para passar argumentos, veja um exemplo:


__new__é um método de classe estático, enquanto __init__é um método de instância. __new__tem que criar a instância primeiro, então __init__pode inicializá-la. 
Observe que __init__leva selfcomo parâmetro. Até que você crie uma instância, não há arquivos self.


#Link Youtube:
#  https://www.youtube.com/watch?v=-zsV0_QrfTw
#  5:25
"""