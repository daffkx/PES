#Lista 6, Exercício 9

import pickle

class Pessoa:
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
    print("\nCadastro de Pessoas")
    print("-------------------")
    print("1 - Cadastrar")
    print("2 - Listar")
    print("3 - Excluir")
    print("4 - Atualizar")
    print("5 - Salvar")
    print("6 - Carregar")
    print("0 - Sair")

    opcao = int(input("Opção: "))

    if opcao == 1:
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        altura = float(input("Altura: "))
        peso = float(input("Peso: "))

        pessoas.append(Pessoa(nome, idade, altura, peso))
        print("Pessoa cadastrada com sucesso!")

    elif opcao == 2:
        if len(pessoas) == 0:
            print("Nenhuma pessoa cadastrada.")
        else:
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

    elif opcao == 5:
        with open("pessoas.pkl", "wb") as arquivo: #wb = write binary
            pickle.dump(pessoas, arquivo) #pickle.dump() grava um objeto python no arquivo

        print("Dados salvos com sucesso!")

    elif opcao == 6:
        try:
            with open("pessoas.pkl", "rb") as arquivo: #rb = read binary
                pessoas = pickle.load(arquivo) #pickle.load() lê um objeto python do arquivo

            print("Dados carregados com sucesso!")

        except FileNotFoundError:
            print("Arquivo não encontrado.")

    elif opcao == 0:
        print("Saindo do programa...")
        break

    else:
        print("Opção inválida!")