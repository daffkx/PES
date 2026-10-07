#Lista 6, Exercício 6

class pessoa:
    def __init__(self, nome, idade, altura, peso):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso

    def mostrar_tudo(self):
        return f"NOME - {self.nome}, IDADE - {self.idade}, ALTURA - {self.altura}, PESO - {self.peso}"

    def imc(self):
        return self.peso / (self.altura ** 2)

    def mostrar_imc(self):
        return f"NOME - {self.nome}, IMC - {self.imc():.2f}"

pessoas = []

while True:
    print("Cadastro de Pessoas")
    print("-------------------")
    print("1 - Cadastrar")
    print("2 - Listar")
    print("0 - Sair")

    opcao = int(input("Opção: "))

    if opcao == 1:
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        altura = float(input("Altura: "))
        peso = float(input("Peso: "))

        pessoas.append(pessoa(nome, idade, altura, peso))

        print("Pessoa cadastrada com sucesso!")

    elif opcao == 2:
        for p in pessoas:
            print(p.mostrar_tudo())
            print(p.mostrar_imc())

    elif opcao == 0:
        print("Saindo do programa...")
        break