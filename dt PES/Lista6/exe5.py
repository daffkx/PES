#Lista 6, Exercício 5

class pessoa:
    def __init__(self, nome, idade, altura, peso):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso

    def exibir(self):
        print(self.nome, self.idade, self.altura, self.peso)

    def imc(self):
        return self.peso / (self.altura ** 2)
    
    def mostrar_imc(self):
        return f"{self.nome} - IMC: {self.imc():.2f}"
    
pessoa1 = pessoa("Dafne", 20, 1.70, 60)
pessoa2 = pessoa("Mariana", 25, 1.80, 80)
pessoa3 = pessoa("Veronica", 30, 1.60, 55)

pessoa1.exibir()
print(pessoa1.mostrar_imc())

pessoa2.exibir()
print(pessoa2.mostrar_imc())

pessoa3.exibir()
print(pessoa3.mostrar_imc())