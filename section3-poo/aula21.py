# Sistema Escolar

class Escola():
    def __init__(self, nome, idade, status):
        self.nome = nome
        self.idade = idade 
        self.status = status

    def apresentar(self):
        print(f'Meu nome é {self.nome}')

    def verificar_status(self):
        # print(f'Status: {"ATIVO" if self.status else "INATIVO"}')
        if self.status == True:
            print(f'Status: ATIVO')
        else:
            print(f'Status: INATIVO')

class Aluno(Escola):
    def __init__(self, nome, idade, status, escolaridade):
        super().__init__(nome, idade, status)
        self.escolaridade = escolaridade

    def apresentar(self):
        super().apresentar()
        print('Eu sou um aluno da escola')

class Professor(Escola):
    def __init__(self, nome, idade, status, materia):
        super().__init__(nome, idade, status)
        self.materia = materia

    def apresentar(self):
        super().apresentar()
        print('Eu sou um professor da escola')

class Assistente(Escola):
    def __init__(self, nome, idade, status, bloco):
        super().__init__(nome, idade, status)
        self.bloco = bloco

    def apresentar(self):
        super().apresentar()
        print('Eu sou um(a) assistente da escola')

a1 = Aluno(nome = 'Guilherme', idade = 14, status = True, escolaridade = 8)
p1 = Professor('Claudia', 40, True, 'Português')
as1 = Assistente('Carlos', 20, False, 'Bloco C')

a1.apresentar()
a1.verificar_status()
# p1.apresentar()
# as1.apresentar()