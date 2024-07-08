# Normalmente o __init__ é o primeiro metodo a ser criado, porém isso não ocorre quando existe o metodo __new__ no objeto
class Foo:
    def __new__(cls):
        print('print do new Foo') 
    def __init__(self):
        print('print do init Foo')

# Nesse caso a função new será chamada e o init será ignorado
F = Foo()

# Para evitar que o init seja ignorado, precisamos criar ele dentro do objeto
class Bar:
    def __new__(cls):
        print('print do new antes de criar a instancia')
        instancia = object.__new__(cls) # 'object' é a super class de todas as class, usamos o metodo __new__ dela para criar um objeto. Nesse caso também funcionaria apenas return super().__new__(cls)
        print('print do new depois de criar a instancia')
        return instancia

    def __init__(self):
        print('print do init Bar')

b = Bar()