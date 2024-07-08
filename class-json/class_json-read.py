from class_json import livro, CAMINHO_ARQUIVO
import json

with open(CAMINHO_ARQUIVO, 'r') as livro_viola:
    viola = json.load(livro_viola)

obj_viola = livro(**viola)

print(obj_viola.nome)
print(obj_viola.qtd_paginas)
print(obj_viola.cor)