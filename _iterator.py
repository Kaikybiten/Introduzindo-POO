# Criando uma instancia iteravel
from _collections_abc import Sequence


class MyList(Sequence):
    def __init__(self):
        self._dados = {}
        self.__index = 0
        self.__next_item = 0

    # Adicionando valores a lista sempre nos ultimos indices
    def append(self, *valor):
        for v in valor:
            self._dados[self.__index] = v
            self.__index += 1

    # Retorna o tamanho da lista
    def __len__(self) -> int:
        return self.__index

    # Retorna o item no index desejado
    def __getitem__(self, index):
        return self._dados[index]

    # Setar o valor de um index especifico
    def __setitem__(self, index, valor):
        self._dados[index] = valor

    # Dando função next para realizar uma iteração sequencial
    def __next__(self):
        if self.__next_item < self.__index:
            valor = self._dados[self.__next_item]
            self.__next_item += 1
            return valor
        raise StopIteration('Não há mais itens para retornar')


lista = MyList()

lista.append('maria')
lista.append('debora', 'felipe')
lista.append('carlos', 'paula')

print(len(lista))
print(lista[0])

print(lista)
print()
print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))
