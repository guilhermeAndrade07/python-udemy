# Escreva um programa que peça ao usuário um número e diga se ele é positivo, negativo ou zero

number = float(input('Digite um número: '))

if number > 0:
    print('Positivo')
elif number == 0:
    print('Zero')
else:
    print('Negativo')