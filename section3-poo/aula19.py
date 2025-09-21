class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f'O meu nome é {self.nome} e tenho {self.idade} anos de idade.')


class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo):
        super().__init__(nome,idade)
        self.cargo = cargo

    def trabalhar(self):
        print(f'- {self.nome} está trabalhando de {self.cargo}.')


class Cliente(Pessoa):
    def __init__(self, nome, idade, saldo):
        super().__init__(nome,idade)
        self.saldo = saldo

    def comprar(self, valor_compra):
        if valor_compra <= self.saldo:
            self.saldo -= valor_compra
            print(f'Olá {self.nome}, a sua compra de R${valor_compra} foi aprovada! Seu saldo atual é de R${self.saldo}')
        else:
            print(f'Olá {self.nome}, saldo insuficiente!!')

f1 = Funcionario('Guilherme', 20, 'Recepcionista')
#f1.apresentar()
#f1.trabalhar()

c1 = Cliente('Caio', 40, 200)
c2 = Cliente('Joaquim', 9, 300)
#c1.apresentar()
c1.comprar(50)
c2.comprar(200)