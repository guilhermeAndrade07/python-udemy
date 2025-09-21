# Crie um dicionário que armazene o nome, idade e cidade de uma pessoa e exiba essas informações de forma organizada.

dados_pessoais = {
    'Nome': input('Digite seu nome: '),
    'Idade':  int(input('Digite sua idade: ')),
    'Cidade':  input('Digite sua cidade: '),
}

print(f"Nome: {dados_pessoais['Nome']}.")
print(f"Idade: {dados_pessoais['Idade']}.")
print(f"Cidade: {dados_pessoais['Cidade']}.")
