# VARIÁVEIS

nome = 'Guilherme'  # string
sobrenome = 'Andrade'  # string
idade = 20  # int
altura = 1.71  # float
desenvolvedor = True  # boolean

# print(nome, sobrenome, 'tem', idade, 'anos.')
# print(nome, 'tem', altura, 'de altura.')
# print(type(nome))
# print(type(idade))
# print(type(altura))
# print(type(desenvolvedor))


name = input("Qual o seu nome: ")
idade = input('Qual a sua idade: ')
fruta_favorita = input('Qual a sua fruta favorita? ')
# sem o f-string
# print(name, 'tem', idade, 'anos de idade.') 
# print(name + ', tem', idade, 'anos de idade') 

# f-string
print(f'Olá {name}, você tem {idade} anos de idade e a sua fruta favorita é {fruta_favorita}.')
print(f'Olá {name}, daqui 5 anos você tera {idade + 5} de idade.')
