class Carrinho:
    def __init__(self):
        self._produtos = []

    def inserir_produtos(self, *produtos):
        for produto in produtos: 
            self._produtos.append(produto)

    def total(self):
        total = sum(p._preco for p in self._produtos)
        print(total)

    def listar(self):
        for produto in self._produtos:
            print(f'Produto: {produto._nome}', f'Preço: {produto._preco}', sep='\n')
            print()

class Produto:
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco


p1 = Produto('banana', 3.20)
p2 = Produto('maça', 1.20)

carrinho = Carrinho()

carrinho.inserir_produtos(p1,p2)

carrinho.listar()

carrinho.total()
