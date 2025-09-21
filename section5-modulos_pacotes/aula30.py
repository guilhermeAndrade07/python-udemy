# PACOTES/BIBLIOTECAS não padrão (via pip):

'''
Para instalar (uma única vez):
!pip install nome_pacote

- numpy: computação númerica eficiente
- pandas: análise e manipulação de dados
- matplotlib: criação e visualização de gráficos
- tensorflow: ml e redes neurais no python
entre outras...
'''

import pandas as pd

# print(dir(pd))
# help(pd.read_csv)
# Documentação: https://pandas.pydata.org/docs/

# Criando um DataFrame a partir de um dicionário
dados = {
    'Nomes': ['Guilherme', 'Joaquim', 'Gobato', 'Marcel'],
    'Idades': [20, 9, 2, 42],
    'Cidade': ['São Caetano', 'Santo André', 'Mogi Mirim', 'São Paulo']
}

df = pd.DataFrame(dados)
# print('DataFrame Criado: ')
# print(df)

# Acessando uma coluna específica
# print("\nColuna 'Nomes': ")
# print(df['Nomes'])
# print(df[df['Nomes']== 'Guilherme']) # linha do Guilherme

# Adicionar uma nova coluna:
df['Empregados'] = [True, False, False, True]
print("\nDataFrame após adicionar nova coluna:")
print(df)

# Filtrar os dados
# Buscar linha somente dos empregados
empregados = df[df['Empregados']== True]
print("\nPessoas empregadas:")
print(empregados)