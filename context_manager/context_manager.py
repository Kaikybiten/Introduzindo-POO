class MyContextManeger:
    def __init__(self, caminho, modo):
        self.caminho = caminho
        self.modo = modo
        self.arquivo = None
    
    def __enter__(self):
        print('Abrindo arquivo')
        self.arquivo = open(self.caminho, self.modo)
        return self.arquivo
    
    def __exit__(self, class_exception, exception_, traceback_): # Argumentos para caso seja gerada uma exceção ao fechar o arquivo
        exception_.add_note('Nota da exceção\n')

        print('Fechando arquivo')
        self.arquivo.close()

with MyContextManeger('context_manager\\context_maneger.txt', 'w') as arquivo:
    print('Escrevendo')
    arquivo.write('Linha 1 \n')
    arquivo.write('Linha 2 \n', 123)
    arquivo.write('Linha 3 \n')