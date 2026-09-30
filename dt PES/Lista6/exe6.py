class Pessoa:

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

    pessoa = Pessoa(nome, idade, altura, peso)

    pessoas.append(pessoa)
    
    elif opcao == 2:

        for pessoa in pessoas:
            pessoa.exibir()
            print(pessoa.mostrar_imc())

    elif opcao == 0:
        break

