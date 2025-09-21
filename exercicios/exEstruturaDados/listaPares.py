# Crie uma lista com os números de 1 a 10 e imprima apenas os números pares
números = [1, 2, 3, 4, 5, 6 , 7, 8, 9, 10]
print('Os números pares são: ')
for pares in números:
    if pares % 2 == 0:
        print(pares)