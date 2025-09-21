# Escreva um programa que calcule a soma de todos os números pares de 1 a 100 utilizando um loop for

soma_pares = 0
for numero in range(1, 101):
    if numero % 2 == 0:
        soma_pares += numero
print(f'A soma de todos os número pares de 1 a 100 é igual a {soma_pares}')
