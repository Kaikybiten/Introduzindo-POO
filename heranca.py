class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

class Aluno(Pessoa):
    def definir_nota(self, nota):
        self.nota = nota

carlo = Aluno('carlo', 'miguel')

carlo.definir_nota(6)

print(carlo.nome)
print(carlo.sobrenome)
print(carlo.nota)