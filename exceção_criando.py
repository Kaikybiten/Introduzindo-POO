# Criando exceção
class MeuError(Exception): # 'nome' + error, é uma convenção para nomear exceções
    ...

class MeuOutroError(Exception):
    ...

def levantar_excecao(excecao: Exception):
    raise excecao('Lançando exceção')

# Tratando exceção
try:
    levantar_excecao(MeuError)
except MeuError as error:
    print(error.__class__.__name__) # Nome do tipo do erro
    print(error) # Nome do erro
    levantar_excecao(MeuOutroError) # During handling of the above exception, another exception occurred:
                                    # Durante o tratamento da exceção acima, ocorreu outra exceção:
                                    