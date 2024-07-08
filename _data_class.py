from dataclasses import dataclass, asdict, astuple


# Vacilita a criação de classes simples, sem um init ou repr
@dataclass
class Pessoa:
    nome: str
    sobrenome: str

    # Chamado logo após o init
    def __post_init__(self):
        self.nome_completo = f'{self.nome} {self.sobrenome}'


p1 = Pessoa('Kaiky', 'Bitencourt')
print(p1.nome)
print(p1.sobrenome)
print(p1.nome_completo)

print(p1)  # A dataclass já cria um __repr__ (uma representação da instancia)
print()
print(astuple(p1))  # Porém o modulo tem funções que retornam como uma tupla
print()
print(asdict(p1))  # E que retornam como um dict
print(asdict(p1).keys())
print(asdict(p1).values())
print(asdict(p1).items())


# Quando o init for definido com False, será necessario cria-lo, não podendo
# utilizar o post init
@dataclass(init=False)
class Animal:
    def __init__(self, especie, nome):
        self.especie = especie
        self.nome = nome


# Também posibilita que os dados de uma classe sejam imutaveis
@dataclass(frozen=True)
class Familia:
    pai: str
    mae: str


f1 = Familia('helio', 'joelma')
# f1.pai = 'carlos'
# f1.mae = 'felicia'
