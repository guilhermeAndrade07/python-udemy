# Arquivo CSV

import csv

dados = [["Nome", "Idade"], ["Gui", 20], ["Quim", 9], ["Gobato", 2]]

with open("dados.csv", "w", newline="") as arquivo_csv:
    escritor = csv.writer(arquivo_csv)
    escritor.writerows(dados)


with open("dados.csv", "r") as arquivo_csv:
    leitor = csv.reader(arquivo_csv)
    for linha in leitor:
        print(linha)
