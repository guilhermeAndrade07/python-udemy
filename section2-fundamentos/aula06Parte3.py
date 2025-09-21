# Controle de LOOPS --> Break / Continue / Pass

# Break --> A declaração break é usada para terminar um loop completamente e imediatamente

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
alvo = 5
for numero in numeros:
    print(f"Verificando o número: {numero}")
    if numero == alvo:
        print("Encontrei o número 5! Saindo do loop.")
        break # Sai do loop for
print("Fim do programa.")

print('---------------------------')

# Continue --> A declaração continue pula o restante do código dentro do loop para a iteração atual e move para a próxima iteração do loop. 

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for numero in numeros:
    if numero % 2 != 0: # Se o número for ímpar...
        continue # ...pula para a próxima iteração
    print(f"Número par encontrado: {numero}")
print("Fim do programa.")

print('---------------------------')

# Pass --> A declaração pass é um "não-faz-nada" em Python. Ela serve como um espaço reservado para um bloco de código que ainda não foi implementado

numeros = [1, 2, 3, 4, 5]
for numero in numeros:
    if numero > 3:
        # Futuramente, a lógica para números maiores que 3 estará aqui.
        pass
    else:
        print(f"Processando número: {numero}")
print("Fim do programa.")