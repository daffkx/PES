#Lista 7, Exercício 2

class CPU:
    def __init__(self, fabricante, modelo):
        self.fabricante = fabricante 
        self.modelo = modelo

class Computador:
    def __init__(self, tipo, fabricante, modelo):
        self.tipo = tipo
        self.cpu = CPU(fabricante, modelo)

computador = Computador("Desktop", "Intel", "i7")

print(f"Tipo de computador: {computador.tipo}")
print(f"Fabricante de CPU: {computador.cpu.fabricante}")
print(f"Modelo de CPU: {computador.cpu.modelo}")