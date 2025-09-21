# Listas / Tuplas / Dicionarios

# DICIONARIOS --> Armazena informações de: usuários, endereços, produtos, configurações. Usa-se {chaves}
# usuario = {
#        'Nome': 'Guilherme',
#        'Idade': 20,
#        'departamento': 'TI'
#}
# print(usuario['nome'])
# usuario['Idade'] = 21 # Modificando o valor
# usuario['Cidade'] = 'SJRP'
# print(usuario)

# Exemplo dia a dia

aluno = {
    'Nome': input('Nome do aluno: '),
    'Idade': int(input('Idade do aluno: ')),
    'Curso': input('Curso do aluno: '),
}

print(f'{aluno['Nome']} tem {aluno['Idade']} anos e está fazendo o curso de {aluno['Curso']}.')
