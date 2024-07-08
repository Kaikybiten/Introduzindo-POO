def adiciona_repr(cls):
    def my_repr(self):
        class_nome = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_nome}{class_dict}'
        return class_repr
    cls.__repr__ = my_repr # Define o repr da class como a função my_repr
    return cls # Retorna a mesma class, porém decorada (a class foi sobreescrita)

@adiciona_repr
class Planeta:
    def __init__(self, nome):
        self.nome = nome 
    
@adiciona_repr
class Time:
    def __init__(self, nome):
        self.nome = nome
    
flamengo = Time('time')
plutao = Planeta('plutão')

print(plutao)
print(flamengo)