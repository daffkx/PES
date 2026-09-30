#Lista 6, Exercício 2

class carro:
    def __init__(self, marca, cor):
        self.marca = marca
        self.cor = cor

    def pintar(self, nova_cor):
        self.cor = nova_cor
    
    def mostrar(self):
        return self.cor
    
carro1 = carro("BMW", "Preto")

carro1.pintar("Branco")

print(carro1.mostrar())