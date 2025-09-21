# Listas / Tuplas / Dicionarios

# LISTAS --> Quando preciso de varios itens mutáveis(pode adiconar, alterar, remover) e usa-se os [colchetes]

# frutas = ['Laranja', 'Abacaxi', 'Banana', 'Morango']
# print(frutas[0]) # Baseado em index, inicia do Zero
# frutas.append('Uva verde') # Adiciona o item no final da lista
# frutas.remove('Laranja') # Remove a fruta 
# print(len(frutas)) # Lê quantos itens tem na lista
# print(frutas)

# Exemplo do dia a dia
print('TAREFAS DIÁRIAS:')
tarefas = []
tarefas.append('Estudar Python com Ia')
tarefas.append('Tomar banho')
tarefas.append('Fazer Almoço')
tarefas.append('Ir trabalhar')
for itens in tarefas:
    print(f'- {itens}')

