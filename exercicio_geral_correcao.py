from abc import abstractmethod, ABC


class Conta(ABC):
    def __init__(self, num_agencia: int, num_conta: int):
        self.num_conta: int = num_conta
        self.num_agencia: int = num_agencia
        self.saldo: float = 0

    def __repr__(self) -> str:
        return f'{__class__.__name__}\nAgência: {self.num_agencia}\n'\
            f'Conta: {self.num_conta}\nSaldo: R$ {self.saldo:.2f}'

    def detalhes(self, msg: str = ''):
        print(f'Seu saldo atual é {self.saldo:.2f}. {msg}.')

    def depositar(self, valor: float) -> float:
        self.saldo += valor
        self.detalhes('Deposito realizado com sucesso.')
        return self.saldo

    @abstractmethod
    def sacar(self, saque: float) -> float:
        return self.saldo


class Pessoa:
    def __init__(self, nome: str, idade: int):
        self._nome = nome
        self._idade = idade
        self._conta = None

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, name: str):
        self._nome = name

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade: int):
        self._idade = idade

    def __repr__(self) -> str:
        return f'Nome: {self._nome}\nIdade: {self._idade}'


class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int):
        super().__init__(nome, idade)
        self.conta: Conta

    def atribuir_conta(self, conta: Conta):
        self._conta = conta


class ContaPopanca(Conta):
    def sacar(self, saque: float) -> float:
        if self.saldo >= saque:
            self.saldo -= saque
            self.detalhes('Saque realizado com sucesso.')
            return self.saldo
        self.detalhes('Saldo indisponivel.')
        return self.saldo


class ContaCorrente(Conta):
    def sacar(self, saque: float) -> float:
        if self.saldo - saque <= -500:
            self.detalhes('Saldo Indisponivel.')
            return self.saldo
        self.saldo -= saque
        self.detalhes('Saque realizado com sucesso.')
        return self.saldo


class Banco():
    def __init__(self, nome: str):
        self._nome = nome
        self.clientes: list[Cliente] = []
        self.contas: list[Conta] = []
        self.agencias: list[int] = []

    def adiciona_cliente(self, cliente: Cliente):
        if isinstance(cliente, Cliente):
            self.agencias.append(cliente._conta.num_agencia)
            self.contas.append(cliente._conta)
            self.clientes.append(cliente)

    def __validar_cliente(self, cliente: str) -> Cliente | None:
        cliente_registrado = [c for c in self.clientes if c.nome == cliente]

        if not (cliente_registrado) or \
                cliente not in cliente_registrado[0]._nome:
            print('Esse nome não pertece a nenhum de nossos clientes')
            return
        return cliente_registrado[0]

    def __validar_agencia(self, agencia: int) -> int | None:
        if agencia not in self.agencias:
            print('Essa agencia não faz parte desse banco')
            return
        return agencia

    def __validar_conta(
            self, cliente: Cliente | None,
            conta: int
    ) -> Conta | None:
        conta_registrada = [c for c in self.contas if c.num_conta == conta]

        if not conta_registrada or conta != conta_registrada[0].num_conta:
            print('Essa conta não faz parte desse banco')
            return
        if not isinstance(cliente, Cliente) \
                or conta_registrada[0] != cliente._conta:
            print('Essa conta não pertence a esse cliente')
            return
        return conta_registrada[0]

    def __autenticar(self) -> Conta | None:
        cl = input('Insira seu nome: ')
        cl = self.__validar_cliente(cl)
        if cl is None:
            return

        ag = int(input('Insira o numero da sua agencia: '))
        ag = self.__validar_agencia(ag)
        if ag is None:
            return

        cnt = (int(input('Insira o numero da sua conta: ')))
        cnt = self.__validar_conta(cl, cnt)
        if cnt is None:
            return

        return cnt

    def fazer_deposito(self):
        conta_registrada = self.__autenticar()
        if not isinstance(conta_registrada, Conta):
            return
        deposito = input('Insira o valor que deseja depositar: ')
        deposito = float(deposito)
        conta_registrada.depositar(deposito)

    def fazer_saque(self):
        conta_registrada = self.__autenticar()
        if not isinstance(conta_registrada, Conta):
            return
        saque = input('Insira o valor que deseja sacar: ')
        saque = float(saque)
        conta_registrada.sacar(saque)


c1 = ContaCorrente(123, 4567)
print(c1)

joao = Cliente('k', 19)
print(joao)

joao.atribuir_conta(c1)

santander = Banco('Santander')
santander.adiciona_cliente(joao)

santander.fazer_deposito()
santander.fazer_saque()
