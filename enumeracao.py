import enum

class Direcoes(enum.Enum):
    ESQUERDA = 1
    DIREITA = 2
    BAIXO = 4
    CIMA = 3
    
# Chamando o enum...
print(Direcoes(1)) # Pela numeração
print(Direcoes.ESQUERDA) # Pela chave

print(Direcoes(1).name) # Retorna apenas o nome da chave
print(Direcoes.ESQUERDA.value) # Retorna apenas a numerção da chave


def mover(direcao: Direcoes):
    if not isinstance(direcao, Direcoes):
        raise TypeError('Direção desconhecida')
    print(f'movendo para {direcao.name}')

mover(Direcoes(1))
mover(Direcoes.DIREITA)