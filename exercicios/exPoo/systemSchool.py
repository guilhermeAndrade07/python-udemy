# School system with POO


class RegisterSchool():
    def __init__(self, nome, idade, sexo, cpf, email):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.cpf = cpf
        self.email = email

    def presentation(self):
        print("-------------------------------")
        print(f"Dados do Usuário: ")
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Sexo: {self.sexo}")
        print(f"CPF: {self.cpf}")
        print(f"E-mail: {self.email}")

class Teacher(RegisterSchool):
    def __init__(self, nome, idade, sexo, cpf, email, materia, vinculo):
        super().__init__(nome, idade, sexo, cpf, email)
        self.materia = materia
        self.vinculo = vinculo

    def presentation(self):
        super().presentation()
        print(f"Matéria: {self.materia}")
        print(f"Vínculo: {self.vinculo}")

class Student(RegisterSchool):
    def __init__(self, nome, idade, sexo, cpf, email, turma):
        super().__init__(nome, idade, sexo, cpf, email)
        self.turma = turma

    def presentation(self):
        super().presentation()
        print(f"Turma: {self.turma}")

while True:
    print("-- CADASTRO --")
    print("Qual tipo de cadastro será:")
    print("1 - Professor")
    print("2 - Aluno")
    option = input("Digite sua escolha: ")

    nome = input("Nome completo: ")
    idade = int(input("Idade: "))
    sexo = input("Sexo: ")
    cpf = float(input("CPF: "))
    email = input("E-mail: ")

    if option == "1":
        materia = input("Máteria de formação: ")
        vinculo = input("Vinculo de contrato: ")
        print("-----------------------------")
        cadastro = Teacher(nome, idade, sexo, cpf, email, materia, vinculo)

    elif option == "2":
        turma = input("Turma matriculada: ")
        print("-----------------------------")
        cadastro = Student(nome, idade, sexo, cpf, email, turma)
    else:
        print("Opção inválida")
        cadastro = None

    if cadastro:
        cadastro.presentation()

    continous = input("Deseja realizar um novo cadastro? (sim/não)\n").lower()

    if continous != "sim":
        break