# property  é um metodo que pode ser usado como atributo
# Usada para mudar o nome de um atributo sem afetar os codigo clientes
class Caneta:
    def __init__(self, cor, tamanho):
        self._cor = cor
        self._tamanho = tamanho

    @property
    def cor(self):
        return self._cor
    
    # O property impede a definição do valor de um atributo de uma instancia "c1.cor = 'verde'"
    # Por iss criamos um setter
    @cor.setter
    def cor(self, valor): 
        self._cor = valor 

    @property
    def tamanho(self):
        return self._tamanho

    # Setter também pode ser usado para definir condições de um atributo
    @tamanho.setter
    def tamanho(self, valor):
        if valor < 0:
            raise ValueError('A caneta não pode ter um tamanho negativo')
        self._tamanho = valor


c1 = Caneta('azul', 20)

print(c1.cor)

c1.cor = 'verde'

print(c1.cor)

c1.tamanho = -20

