class cachorro:
    def __init__(self, nome, raca, cor):
        self.nome   =   nome
        self.raca   =   raca
        self.cor    =   cor

billy = cachorro('billy', 'vira-lata', 'preto')

print(billy.nome)
print(billy.raca)
print(billy.cor)