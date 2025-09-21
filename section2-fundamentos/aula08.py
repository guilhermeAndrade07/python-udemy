# FUNÇÃO --> def

# def saudacao(nome):
#     print(f'Olá {nome}, vamos aprender Python com AI')
# saudacao('Guilherme')


# def somar(x, y):
#     return x + y
# soma = somar(10, 5)
# print(f'A soma de 10 + 5 é igual a {soma}')

def calcular_desconto(preco, desconto):
    return preco - (preco * desconto / 100)

final = calcular_desconto(120, 10)
print(f'O valor final com o desconto é de R${final:.2f}')