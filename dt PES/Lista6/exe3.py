#Lista 6, Exercício 3

class conta_bancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo = self.saldo + valor

    def sacar(self, valor):
        self.saldo = self.saldo - valor

    def mostrar_saldo(self):
        return self.saldo

conta1 = conta_bancaria("Dafne", 1000)

conta1.depositar(500)

conta1.sacar(100)

print(conta1.mostrar_saldo())