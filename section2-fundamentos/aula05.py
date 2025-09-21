# CONDIÇÕES -> IF ELIF ELSE
# IF, ELSE --> Se, Se não

# numero = int(input('Digite um número: '))
# if numero == 10:
#     print('Acertou o número')
# else:
#     print('Errou o número é diferente')


# IF, ELIF, ELSE --> 

# nota_aluno = float(input('Digite sua nota: '))
# if nota_aluno >= 7:# 
#     print('Você foi aprovado!')
# elif nota_aluno >= 5:# 
#     print('Você está de recuperação!')
# else:
#     print('Você foi reprovado!')


# nome_usuario = input('Digite seu usario: ')
# senha_usuario = input('Digite sua senha: ')
# if nome_usuario == 'Admin' and senha_usuario == '123admin':
#     print('Login permitido!')
# else:
#     print('ERRO! Usuario ou senha incorretos!')


idade = int(input('Qual a sua idade? '))
autorizacao_pais = input('Tem a autorização dos pais? (Sim/Não): ')
if idade >= 18:
    print('Está AUTORIZADO!')
elif idade >= 16 and autorizacao_pais == 'Sim':
    print('Está autorizado pelos pais!')
else:
    print('Não está autorizado!')