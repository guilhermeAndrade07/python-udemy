'''
Módulos e Pacotes são recursos fundamentais
para organizar e utilizar o código de forma eficiente.

Eles adicionam funcionalidades prontas para o uso,
permitindo que se realize tarefas complexas
com poucas linhas de código
'''

# MÓDULOS
# Os módulos padrões mais conhecidos no python (Não precisam instalar)
'''
- os: usado para interagir com sistema operacional
- math: fornece funções matemáticas básicas
- random:  geração de números aleatórios
- datetime: manipulação de datas e horários
entre outras...
'''

# EXEMPLO 1
import random

# print(dir(random)) # mostra tudo que tem
# help(random.randint) # Descrição detalhada

numero_aleatorio = random.randint(1, 100) # Chama a função
print(f'O número aleatório escolhido de 1 a 100 foi: {numero_aleatorio}')

lista = ['Porshe', 'Mercedes', 'BMW', 'Lamborghini', 'Nissan', 'Pagani']
carro_aleatorio = random.choice(lista)
print(f'Hoje irei usar um carro da {carro_aleatorio}')


# EXEMPLO 2
import math

# print(dir(math))
# help(math.sqrt)

# calcular raiz quadrada
numero = int(input('Digite um número: '))
raiz_quadrada = math.sqrt(numero)
print(f'A raiz quadrada de {numero} é {raiz_quadrada:.3}')