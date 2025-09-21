# Polymorphism Parte 2

class Cachorro:
    def emitir_som(self):
        print(f'Au Au Au')

class Gato:
    def emitir_som(self):
        print(f'Miau')

animais = [Cachorro(), Gato()]

for animal in animais:
    animal.emitir_som()