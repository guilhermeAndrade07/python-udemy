# Crie um programa que leia dois números do usuário e exiba a soma, subtração, multiplicação e divisão desses números.

number1 = int(input('Digite o primeiro número: '))
number2 = int(input('Digite o segundo número: '))
soma = number1 + number2
print(f'A soma de {number1} + {number2} = {soma}')
subtracao = number1 - number2
print(f'A subtração de {number1} - {number2} = {subtracao}')
multi = number1 * number2
print(f'A multiplicação de {number1} * {number2} = {multi}')
divisao = number1 / number2
print(f'A divisão de {number1} / {number2} = {divisao}')