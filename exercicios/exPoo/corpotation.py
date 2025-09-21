# Sistema Corporativo

class Cadastro():
    def __init__(self, nome, idade, cargo, nivel):
        self.nome = nome
        self.idade = idade
        self.cargo = cargo
        self.nivel = nivel

    def apresentacao(self):
        print(
            f"- Meu nome é {self.nome} tenho {self.idade} anos de idade. \n Atuo na área de {self.cargo}, sou {self.nivel}.")

class Desenvolvedores(Cadastro):
    def __init__(self, nome, idade, cargo, nivel, linguagem):
        super().__init__(nome, idade, cargo, nivel)
        self.linguagem = linguagem

    def apresentacao(self):
        super().apresentacao()
        print(f"Utilizo {self.linguagem} como linguagem de programação.")
        print("--------------------------------------------------------")

class Rh (Cadastro):
    def __init__(self, nome, idade, cargo, nivel, funcionalidade):
        super().__init__(nome, idade, cargo, nivel)
        self.funcionalidade = funcionalidade

    def apresentacao(self):
        super().apresentacao()
        print(f"Minha função dentro do Rh é {self.funcionalidade}.")
        print("--------------------------------------------------")

class Equipe_vendas (Cadastro):
    def __init__(self, nome, idade, cargo, nivel, funcionalidade):
        super().__init__(nome, idade, cargo, nivel)
        self.funcionalidade = funcionalidade

    def apresentacao(self):
        super().apresentacao()
        print(
            f"Minha função dentro da equipe de vendas é {self.funcionalidade}.")
        print("----------------------------------------------------------------")


cadastro1 = Desenvolvedores(nome="Guilherme", idade=20,cargo="Desenvolvedor", nivel="Estágiario", linguagem="Python")
cadastro2 = Rh(nome="Junior", idade=25, cargo="Rh", nivel="Pleno", funcionalidade="Gestão de Pessoas")
cadastro3 = Equipe_vendas(nome="Leonardo", idade=30, cargo="Equipe de Vendas",nivel="Senior", funcionalidade="Negociação e Fechamento de Vendas")

cadastro1.apresentacao()
cadastro2.apresentacao()
cadastro3.apresentacao()
