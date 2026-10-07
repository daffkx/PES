#Lista 6, Exercício 7

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
    print("3 - Excluir")
    print("4 - Atualizar")
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

    elif opcao == 3:
        nome_excluir = input("Digite o nome da pessoa que deseja excluir: ")
        for p in pessoas:
            if p.nome == nome_excluir:
                pessoas.remove(p)
                print(f"{nome_excluir} foi excluído com sucesso!")
                break
        else:
            print(f"{nome_excluir} não encontrado.")

    elif opcao == 4:
        nome_atualizar = input("Digite o nome da pessoa que deseja atualizar: ")
        for p in pessoas:
            if p.nome == nome_atualizar:
                p.idade = int(input("Nova idade: "))
                p.altura = float(input("Nova altura: "))
                p.peso = float(input("Novo peso: "))
                print(f"{nome_atualizar} foi atualizado com sucesso!")
                break
        else:
            print(f"{nome_atualizar} não encontrado.")

    elif opcao == 0:
        print("Saindo do programa...")
        break