# POO --> Programação Orientada a objetos
# --> Organizar
# -> Class = classe, grupo de informação, começa com a primeira letra maiuscula

class Casa:
    def __init__(self, cor, quartos, banheiros):
        self.cor = cor #atributo
        self.quartos = quartos #atributo
        self.banheiros = banheiros #atributo

    def mostrar_cor(self):
        print(f'A cor da casa é {self.cor}.')
        
    def mostrar_quartos(self):
        print(f'Está casa tem {self.quartos} quartos.')

    def mostrar_banheiros(self):
        print(f'Está casa tem {self.banheiros} banheiros.')

    def adicionar_quarto(self):
        self.quartos += 1
        print(f'Agora a casa tem {self.quartos} quartos.')

    def pintar_casa(self, nova_cor):
        print(f'Pintando a casa de {self.cor} para {nova_cor}')

casa1 = Casa('Verde', 4, 6)
casa2 = Casa('Azul', 2, 4)

print(f'\nCasa 1 :')
casa1.mostrar_cor()
casa1.mostrar_quartos()
casa1.mostrar_banheiros()
casa1.adicionar_quarto()
casa1.pintar_casa('Branca')

print(f'\nCasa 2 :')
casa2.mostrar_cor()
casa2.mostrar_quartos()
casa2.mostrar_banheiros()
casa2.adicionar_quarto()
casa2.pintar_casa('Preta')