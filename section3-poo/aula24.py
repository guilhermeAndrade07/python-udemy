# Nested

# Criar a classe Main

class Computador:
    def __init__(self, modelo, gpu_nome, gpu_memoria, cpu_nome, cpu_cores, cpu_clock):
        self.modelo = modelo
        self.gpu = self.GPU(gpu_nome, gpu_memoria)
        self.cpu = self.CPU(cpu_nome, cpu_cores, cpu_clock)

    def mostrar_configuracao(self):
        print(f'Computador: {self.modelo}')
        self.gpu.mostar_gpu()
        self.cpu.mostrar_cpu()

    class GPU: # Nested Class
        def __init__(self, nome, memoria_gb):
            self.nome = nome
            self.memoria_gb = memoria_gb 

        def mostar_gpu(self):
            print(f'GPU: {self.nome} - {self.memoria_gb}gb')
            
    class CPU:
        def __init__(self, nome, cores, clock_ghz):
            self.nome = nome
            self.cores = cores
            self.clock_ghz = clock_ghz

        def mostrar_cpu(self):
            print(f'CPU: {self.nome} - {self.cores} nucleos - {self.clock_ghz} GHz')

# Utilização
pc1 = Computador('Dell Vostro', 'NVIDEA RTX 4090', 24, 'Intel Core i3', 3, 4.6)
pc1.mostrar_configuracao()
