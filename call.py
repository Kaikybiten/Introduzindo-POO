class Chamando:
    def __init__(self, telefone):
        self.telefone = telefone

    def __call__(self): # __call__ permite que chame uma instancia
        print(f'discando {self.telefone}...')
        print(f'chamando {self.telefone}...')
        print('ligação concluida')

call01 = Chamando(40028922)

call01() # Chamando...