# OPERADORES RELACIONAIS
# --> Usada para comparar valores e retornar se é TRUE ou FALSE
# == Igual
# != Diferente
# >  Maior que
# <  Menor que
# >= Maior ou igual a
# <= Menor ou igual a

# OPERADORES LÓGICOS
# AND --> E   --> Um e o outro
# OR  --> OU  --> Um ou o outro 
# NOT --> NÃO --> Nem um e nem o outro

# Para dirigir a pessoas tem que ser maior que 18 anos de idade é adulto e ter carteira de motorista
# idade = int(input('Qual a sua idade? '))
# carteira = False
# verificador = idade >= 18 and carteira 
# print(verificador)

usuario = input('Digite o seu usuario: ')
senha = input('Digite a sua senha: ')
login_valido = usuario == 'Admin' and senha == '123admin'
print(f'Login permitido: {login_valido}')