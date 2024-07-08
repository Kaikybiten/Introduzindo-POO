class pessoa:
    def __init__(self, nascimento):
        self.nascimento = nascimento

    def get_idade(self):
        ano_atual = 2024
        return ano_atual - self.nascimento
    
joao = pessoa(2003)

idade = joao.get_idade()
print(idade)