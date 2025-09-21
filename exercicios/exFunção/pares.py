def numeros_pares(lista):
    return list(filter(lambda x: x % 2 == 0 , lista))

def numeros_impares(lista):
    return list(filter(lambda x: x % 2 != 0 , lista))

numeros = [1, 2, 3, 4, 5, 6, 7 ,8 ,9, 10]
resultado_pares = numeros_pares(numeros)
resultado_impar = numeros_impares(numeros)

print(resultado_pares)
print(resultado_impar)