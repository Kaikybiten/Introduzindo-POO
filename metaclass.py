# Toda class em python é do tipo 'type'

from typing import Any


class Foo:
    def __init__(self, nome):
        self.nome = nome

# Argumentos do tipo type são nome, herança, e dicionario do objeto
Bar = type('bar', (object,), {'nome' : 'bar'})

f = Foo('foo')

print(f.nome)

print(Bar.nome)



# A metaclass é executada antes da criação da classe. As metaclasses permitem personalizar a criação de classes, modificando ou adicionando comportamentos durante o processo de criação da classe.
class Meta(type):

    # O __new__ da metaclass é excutado antes da criação da class
    def __new__(cls, name, bases, dct):
        print(f"criando class {name}...")
        classe = super().__new__(cls, name, bases, dct)
    
        if 'falar' not in classe.__dict__ or not(callable(classe.__dict__['falar'])):
            raise NotImplementedError('Implemete a função "falar"')
        return classe
    
    # O __call__ da metaclass é executado quando a class é instanciada
    def __call__(cls, *args, **kwds):
        instancia =  super().__call__(*args, **kwds)
        if 'value' not in instancia.__dict__:
            raise NotImplementedError('Crie o atributo "value"')

# Use o parâmetro metaclass na definição da classe para especificar a metaclass.
class MyClass(metaclass=Meta):
    def __init__(self, value):
        self.value = value
        ...

    def falar(self):
        print('falando')

# Instanciando a classe para ver o resultado
obj = MyClass(10)