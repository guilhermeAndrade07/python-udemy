# HERANÇA

class Animal:
    def __init__(self, nome, cor, especie):
        self.nome = nome
        self.cor = cor
        self.especie = especie

    def apresentar(self):
        print(f'- Eu sou o {self.especie} chamado {self.nome}.')


class Gato(Animal):

    def emitir_som(self):
        print("MIAU!")

    def arranhar(self):
        print("O gato está arranhando")

class Cachorro(Animal):

    def emitir_som(self):
        print("Au Au Au!")


class Elefante(Animal):

    def emitir_som(self):
        print("Pruuuuuuu!")


gato1 = Gato('Félix', 'Branco', 'Siamese')
gato1.apresentar()
gato1.emitir_som()
gato1.arranhar()

cachorro1 = Cachorro('Gobato', 'Cinza e Branco', 'American Bully')
cachorro1.apresentar()
cachorro1.emitir_som()

cachorro2 = Cachorro('Pillow', 'Marrom e Branco', 'Beagle')
cachorro2.apresentar()


elefante1 = Elefante('Dumbo', 'Cinza', 'Elefante Asiatico')
elefante1.apresentar()
elefante1.emitir_som()
