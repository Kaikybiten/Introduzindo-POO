class celular:
    def __init__(self, marca, memoria, cor):
        self.marca = marca
        self.memoria = memoria
        self.cor = cor

cel01 = celular('apple', 500, 'branca')

print(cel01.__dict__)

del cel01.memoria

print(cel01.__dict__)

# Ou melhor
print(vars(cel01))

# É possivel usar um dicionario para definir as variaveis de um objeto

dados = {'marca':'samsung', 'memoria' : 600, 'cor' : 'preta'}

cel02 = celular(**dados)

print(cel02.marca)
print(cel02.memoria)
print(cel02.cor)
print(vars(cel02))