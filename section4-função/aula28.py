# funções embutidas (map, filter, zip)

# MAP
numeros = [1, 2, 3, 4]
dobrados = list(map(lambda x: x * 2, numeros))
print(dobrados)

# FILTER
numerosFilter = [1, 2, 3, 4, 5]
pares = list(filter(lambda x: x % 2 == 0, numerosFilter))
print(pares)  

# ZIP
nomes = ["Ana", "Bruno", "Carlos"]
idades = [25, 30, 35]
combinacao = list(zip(nomes, idades))
print(combinacao)  
