class Planeta:
    def __init__(self, cor, tamanho):
        self.cor = cor
        self.tamanho = tamanho

    # Esse decorator permite que a função seja chamada sem a necessidade de indicar uma instancia
    @classmethod
    def girar(cls):
        print('planeta girando')

    
Planeta.girar()