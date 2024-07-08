import json

class livro:
    def __init__(self, qtd_paginas, cor, nome):
        self.qtd_paginas = qtd_paginas
        self.cor = cor
        self.nome = nome

viola_davis = livro(500, 'preta', 'viola davis')

CAMINHO_ARQUIVO = 'class-json\\viola-davis.json'

def fazer_dump():
    with open(CAMINHO_ARQUIVO, 'w') as livro_viola:
        json.dump(
            viola_davis.__dict__, livro_viola
        )

# ADENDO! como esse modulo está sendo importado em outro modulo, as função que estão aqui serão chamadas ao iniciar o modulo irmão para impedir isso, segue o codigo a baixo:

if __name__ == '__main__': 
    fazer_dump()
    # Nesse caso só quando esse modulo for inciado sozinho (como o principal 'main'), essas funções serão chamadas,  caso seja iniciado apartir de outro modulo (não será o principal 'main'), não irá chamar as funções do escopo if