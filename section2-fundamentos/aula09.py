
import aula09Parte2  

# aula09Parte2.saudacao('Guilherme')
# print(aula09Parte2.soma(10, 2))

minha_idade = int(input('Digite a sua idade: '))
if aula09Parte2.vericar_maioridade(minha_idade):
    print(f'Você é maior de idade')
else:
    print('Você é menor de idade')