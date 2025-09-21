# Aggregation

class Motor:
    def __init__(self, marca, potencia):
        self.marca = marca
        self.potencia = potencia

class Carro:
    def __init__(self):
        self.motores = []

    def adicionar_motor(self, motor):
        self.motores.append(motor) # append = adicionar

    def listar_motores(self):
        for motor in self.motores:
            print(f'Marca: {motor.marca} - {motor.potencia} cavalos')


# Criando o Motor (Objetos)
motor_v6 = Motor('Ford', 300)
motor_v8 = Motor('Ferrari', 650)
motor_v12 = Motor('McLaren', 900)

# Criar o carro e adicionar o motor
carro1 = Carro()
carro1.adicionar_motor(motor_v6)
carro2 = Carro()
carro2.adicionar_motor(motor_v8)
carro3 = Carro()
carro3.adicionar_motor(motor_v12)

# Listar os Motores
carro1.listar_motores()
carro2.listar_motores()
carro3.listar_motores()