# Sistema Corporativo

class Cadastro():
    def __init__(self, nome, idade, cargo, nivel):
        self.nome = nome
        self.idade = idade
        self.cargo = cargo
        self.nivel = nivel

    def apresentacao(self):
        print(
            f"- Meu nome é {self.nome}, tenho {self.idade} anos de idade. \n Atuo na área de {self.cargo}, sou {self.nivel}.")

class Desenvolvedores(Cadastro):
    def __init__(self, nome, idade, cargo, nivel, linguagem):
        super().__init__(nome, idade, cargo, nivel)
        self.linguagem = linguagem

    def apresentacao(self):
        super().apresentacao()
        print(f" Utilizo {self.linguagem} como linguagem de programação.")
        print("--------------------------------------------------------")

class Rh (Cadastro):
    def __init__(self, nome, idade, cargo, nivel, funcionalidade):
        super().__init__(nome, idade, cargo, nivel)
        self.funcionalidade = funcionalidade

    def apresentacao(self):
        super().apresentacao()
        print(f" Minha função dentro do Rh é {self.funcionalidade}.")
        print("--------------------------------------------------")

class Equipe_vendas (Cadastro):
    def __init__(self, nome, idade, cargo, nivel, funcionalidade):
        super().__init__(nome, idade, cargo, nivel)
        self.funcionalidade = funcionalidade

    def apresentacao(self):
        super().apresentacao()
        print(
            f" Minha função dentro da equipe de vendas é {self.funcionalidade}.")
        print("----------------------------------------------------------------")

while True:
    print("Escolha o seu tipo de cadastro:")
    print("1 - Desenvolvedor")
    print("2 - RH")
    print("3 - Equipe de Vendas")
    opcao = input("Digite o número da opção: ")

    nome = input("Digite seu nome: ")
    idade = int(input("Digite a sua idade: "))
    cargo = input("Qual o seu cargo: ")
    nivel = input("Digite o nível: ")

    if opcao == "1":
        linguagem = input("Digite a linguagem de programação: ")
        cadastro = Desenvolvedores(nome, idade, cargo, nivel, linguagem)
    elif opcao == "2":
        funcionalidade = input("Digite a funcionalidade no RH: ")
        cadastro = Rh(nome, idade, cargo, nivel, funcionalidade)
    elif opcao == "3":
        funcionalidade = input("Digite a funcionalidade na equipe de vendas: ")
        cadastro = Equipe_vendas(nome, idade, cargo, nivel, funcionalidade)
    else:
        print("Opção inválida!")
        cadastro = None

    if cadastro:
        cadastro.apresentacao()

    continuar = input("Deseja cadastrar outro funcionário? (sim/não): ").lower()

    if continuar != "sim":
        break

