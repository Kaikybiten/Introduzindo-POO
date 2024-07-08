class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)
    
    @classmethod
    def anonimo(cls, idade):
        return cls('Anônimo', idade)
    
p1 = Pessoa.criar_com_50_anos('debora')
print(vars(p1))
s
p2 = Pessoa.anonimo(10)
print(vars(p2))