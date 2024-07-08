"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra.

Conta (ABC)
    ContaCorrente
    ContaPoupanca

Pessoa (ABC)
    Cliente
        Clente -> Conta

Banco
    Banco -> Cliente
    Banco -> Conta

Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo 
    Contas devem ter método para depósito 
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar) 
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clentes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
Banco autentica por um método.
"""



from abc import abstractmethod, ABC

class Conta(ABC):
    def __init__(self, agencia, num_conta, saldo):
        self.num_conta = num_conta
        self.agencia = agencia
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    @abstractmethod
    def sacar(self, saque):
        pass

class Pessoa(ABC):
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade
        self._conta = None

    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, name):
        self._nome = name

    @property
    def idade(self):
        return self._idade
    @idade.setter
    def idade(self, idade):
        self._idade = idade

class Cliente(Pessoa):
    def inserir_conta(self, conta):
        self._conta = conta

class ContaPopanca(Conta):
    def sacar(self, saque):
        if self.saldo >= saque:
            self.saldo -= saque
            print(f'Saque de {saque} realizado com sucesso')
        else:
            print('Saldo indisponivel')
        print(f'Seu saldo atual é {self.saldo}')
    
class ContaCorrente(Conta):
    def sacar(self, saque):
        if self.saldo - saque <= -500:
            print('Saldo indisponivel')
        else:
            self.saldo -= saque
            print(f'Saque de {saque} realizado com sucesso')
        print(f'Seu saldo atual é {self.saldo}')
        
class Banco():
    def __init__(self, nome):
        self._nome = nome
        self.clientes = []
        self.contas = []
        self.agencias = []

    def adiciona_cliente(self, cliente):
        if isinstance(cliente, Cliente):
            self.agencias.append(cliente._conta.agencia)
            self.contas.append(cliente._conta.num_conta)
            self.clientes.append(cliente)

    def __validar_conta(self):
        cl = input('Insira seu nome: ')
        cliente_registrado = [c for c in self.clientes if c.nome == cl]
        if cl not in cliente_registrado[0]._nome:
            print('Esse nome não pertece a nenhum de nossos clientes')
            return
        
        ag = input('Insira o numero da sua agencia: ')
        ag = int(ag)
        if (ag not in self.agencias):
            print('Essa agencia não faz parte desse banco')
            return
        
        cnt = input('Insira o numero da sua conta: ')
        cnt = int(cnt)
        if (cnt not in self.contas):
            print('Essa conta não faz parte desse banco')
            return
        return cliente_registrado[0]

    def fazer_deposito(self):
        cliente_registrado = self.__validar_conta()
        cliente_registrado._conta.depositar()

    def fazer_saque(self):
        cliente_registrado = self.__validar_conta()
        saque = input('Insira o valor que deseja sacar: ')
        saque = float(saque)
        cliente_registrado._conta.sacar(saque)

c1 = ContaCorrente(123, 4567, 5000)

joão = Cliente('João', 19)

joão.inserir_conta(c1)

santander = Banco('Santander')

santander.adiciona_cliente(joão)

santander.fazer_saque()