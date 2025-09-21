# Manipulação de Arquivos --> Abrir, ler e escrever arquivos no PYTHON

'''
É utilizado para automatizar edição de textos,
processar logs(registro de um sistema) e armazenar
informações de forma organizada.
'''
# o "w" cria um novo arquivo ou substitui, o "write" é para poder escrever
arquivo = open("exemplo.txt", "w")
arquivo.write("Olá, Python!")
arquivo.close()

# o "r" e "read" é para poder ler o arquivo
# o "with" permite abrir e fechar arquivos de forma automática, tornando o código mais limpo e seguro.
with open("exemplo.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print("Conteúdo do arquivo: ")
    print(conteudo)

# o "a" acrescenta conteúdo no arquivo
with open("exemplo.txt", 'a') as arquivo:
    arquivo.write("\nAbrir, ler e escrever no arquivo")

with open("exemplo.txt", "r") as arquivo:
    conteudo_atualizado = arquivo.read()
    print("\nConteúdo atualizado do arquivo: ")
    print(conteudo_atualizado)