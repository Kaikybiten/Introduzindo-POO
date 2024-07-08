class Pessoa:
    def __init__(self, nome: str, sobrenome: str, idade: int) -> None:
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.nome_completo = f'{nome} {sobrenome}'

    @property
    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'

    @nome_completo.setter
    def nome_completo(self, value: str):
        nome, *sobrenome = value.split()
        self.nome = nome
        self.sobrenome = ' '.join(sobrenome)


p1 = Pessoa('kaiky', 'bitencourt', 20)
print(p1.nome_completo)

p1.nome_completo = 'geovana irineu'
print(p1.nome)
print(p1.sobrenome)
print(p1.nome_completo)
