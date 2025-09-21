# Polymorphism

class Personagens():
    def falar(self):
        print(f'Eu sou um personagem.')

class Guerreiro(Personagens):
    def falar(self):
        print(f'Eu sou um guerreiro forte e destemido!')

class Mago(Personagens):
    def falar(self):
        print(f'Eu sou um mago sábio e poderoso!')
    

class Arqueiro(Personagens):
    def falar(self):
        print(f'Eu sou um arqueiro rápido e destemido!')


# Criar os objetos:

personagens = [Guerreiro(), Mago(), Arqueiro()]

for p in personagens:
    p.falar()