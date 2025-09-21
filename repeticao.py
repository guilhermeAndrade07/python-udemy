# numero = 0
# while numero < 100:
#     numero += 1
#     print(numero)

# numero = 101
# while numero != 0:
#     numero -= 1
#     print(numero)

# soma = 0
# while True:
#     numero = float(input("Digite um número para somar: "))
#     if numero == 0:
#         print(f'Valor da soma = {soma}')
#         break
#     else:
#         soma += numero

tentativas = 0
senha = ' '
while senha != '123admin':
    senha = input("Qual é a senha? ")
    tentativas +=1
    print(f"Tentatica {tentativas}")
print("Acesso liberado!")
print(f"Total de tentativas: {tentativas}")