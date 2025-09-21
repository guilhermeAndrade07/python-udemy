# Crie um conjunto a partir de uma lista que contém elementos duplicados e mostre como os duplicados são removidos.

# Crie uma lista com elementos duplicados
lista_com_duplicados = [10, 20, 30, 40, 20, 50, 60, 10, 30]

print(f"Lista original: {lista_com_duplicados}")
print(f"Número de elementos na lista original: {len(lista_com_duplicados)}")

# Converta a lista para um conjunto para remover os duplicados
conjunto_sem_duplicados = set(lista_com_duplicados)

print(f"\nConjunto após a conversão (duplicados removidos): {conjunto_sem_duplicados}")
print(f"Número de elementos no conjunto: {len(conjunto_sem_duplicados)}")
