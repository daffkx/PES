#Lista 6, Exercício 5

class pessoa:
    def __init__(self, nome, idade, altura, peso):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso

    def mostrar_tudo(self):
        return f"{self.nome}, {self.idade}, {self.altura}, {self.peso}"

    def imc(self):
        return self.peso / (self.altura ** 2)
    
    def mostrar_imc(self):
        return f"{self.nome} - IMC: {self.imc():.2f}"
    
pessoa1 = pessoa("Dafne", 20, 1.70, 60)
pessoa2 = pessoa("Tyler", 25, 1.80, 80)
pessoa3 = pessoa("Josh", 30, 1.60, 55)

pessoa1.mostrar_tudo()
print(pessoa1.mostrar_tudo())

pessoa2.mostrar_tudo()
print(pessoa2.mostrar_tudo())

pessoa3.mostrar_tudo()
print(pessoa3.mostrar_tudo())


pessoa1.mostrar_imc()
print(pessoa1.mostrar_imc())

pessoa2.mostrar_imc()
print(pessoa2.mostrar_imc())

pessoa3.mostrar_imc()
print(pessoa3.mostrar_imc())