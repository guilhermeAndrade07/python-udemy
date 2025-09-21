#  Repetições com for e While

# WHILE --> Quando eu não sei a quantidade de vezes que preciso executar. Vai depender da condição!

i = 0
while i < 5:
    print(i)
    i += 1

senha = ' '
while senha != '123admin':
    senha = input('Qual é a senha? ')
print('Acesso liberado!')