class Pessoa:
    def __init__(self, nome, idade, cargo):
        self.nome = nome
        self.idade = idade
        self.cargo = cargo

    def informacoes(self):
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')
        print(f'Cargo: {self.cargo}')

    def promover(self, novo_cargo):
        print(f'{self.nome} foi provovido(a) para a nova função de {novo_cargo}!')
    
    def atualizar_idade(self, nova_idade):
        if nova_idade > self.idade:
            print(f'Atualizando a idade de {self.idade} para {nova_idade}')
        else:
            print('A nova idade tem que ser maior que a anttiga')

colaborador1 = Pessoa('Guilherme', 20, 'Recepcionista')
colaborador2 = Pessoa('Carlos', 50, 'Dev Pleno')

print(f'\nColaborador 1:')
colaborador1.informacoes()
colaborador1.promover('Estagiario Junior!')
colaborador1.atualizar_idade(22)

print(f'\nColaborador 2:')
colaborador2.informacoes()
colaborador2.promover('Dev Senior!')