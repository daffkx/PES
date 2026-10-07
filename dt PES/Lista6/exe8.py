#Lista 6, Exercício 8

class estudante:
    def __init__(self, matricula, nome, sobrenome, idade):
        self.matricula = matricula
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade

    def apresentar(self):
        return f"MATRÍCULA - {self.matricula}, NOME - {self.nome}, SOBRENOME - {self.sobrenome}, IDADE - {self.idade}"

class professor:
    def __init__(self, matricula, nome, sobrenome, idade, especializacao):
        self.matricula = matricula
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.especializacao = especializacao

    def apresentar(self):
        return f"MATRÍCULA - {self.matricula}, NOME - {self.nome}, SOBRENOME - {self.sobrenome}, IDADE - {self.idade}, ESPECIALIZAÇÃO - {self.especializacao}"

pessoas = []

while True:
    print("Cadastro de Pessoas")
    print("-------------------")
    print("1 - Cadastrar estudante")
    print("2 - Cadastrar professor")
    print("3 - Listar estudantes")
    print("4 - Listar professores")
    print("5 - Alterar estudante pela matricula")
    print("6 - Alterar estudante pelo nome")
    print("7 - Alterar professor pela matricula")
    print("8 - Alterar professor pelo nome")
    print("9 - Excluir estudante pela matricula")
    print("10 - Excluir professor pela matricula")
    print("0 - Sair")

    opcao = int(input("Opção: "))

    if opcao == 1:
        matricula = input("Matrícula: ")
        nome = input("Nome: ")
        sobrenome = input("Sobrenome: ")
        idade = int(input("Idade: "))

        pessoas.append(estudante(matricula, nome, sobrenome, idade))

        print("Estudante cadastrado com sucesso!")

    if opcao == 2:
        matricula = input("Matrícula: ")
        nome = input("Nome: ")
        sobrenome = input("Sobrenome: ")
        idade = int(input("Idade: "))
        especializacao = input("Especialização: ")

        pessoas.append(professor(matricula, nome, sobrenome, idade, especializacao))

        print("Professor cadastrado com sucesso!")

    elif opcao == 3:
        for p in pessoas:
            print(p.apresentar())

    elif opcao == 4:
        for p in pessoas:
            print(p.apresentar())

    elif opcao == 5:
        matricula_atualizar = input("Digite a matrícula do estudante que deseja atualizar: ")
        for p in pessoas:
                p.nome = input("Novo nome: ")
                p.sobrenome = input("Novo sobrenome: ")
                p.idade = int(input("Nova idade: "))
                print(f"Estudante com matrícula {matricula_atualizar} atualizado com sucesso!")
                break
        else:
            print(f"Estudante com matrícula {matricula_atualizar} não encontrado.")

    elif opcao == 6:
         nome_atualizar = input("Digite o nome do estudante que deseja atualizar: ")
         for p in pessoas:
                p.nome = input("Novo nome: ")
                p.sobrenome = input("Novo sobrenome: ")
                p.idade = int(input("Nova idade: "))
                print(f"Estudante com nome {nome_atualizar} atualizado com sucesso!")
                break

    elif opcao == 7:
        matricula_atualizar = input("Digite a matrícula do professor que deseja atualizar: ")
        for p in pessoas:
                p.nome = input("Novo nome: ")
                p.sobrenome = input("Novo sobrenome: ")
                p.idade = int(input("Nova idade: "))
                p.especializacao = input("Nova especialização: ")
                print(f"Professor com matrícula {matricula_atualizar} atualizado com sucesso!")
                break
        else:
            print(f"Professor com matrícula {matricula_atualizar} não encontrado.")

    elif opcao == 8:
        nome_atualizar = input("Digite o nome do professor que deseja atualizar: ")
        for p in pessoas:
                p.nome = input("Novo nome: ")
                p.sobrenome = input("Novo sobrenome: ")
                p.idade = int(input("Nova idade: "))
                p.especializacao = input("Nova especialização: ")
                print(f"Professor com nome {nome_atualizar} atualizado com sucesso!")
                break
        else:
            print(f"Professor com nome {nome_atualizar} não encontrado.")

    elif opcao == 9:
        matricula_excluir = input("Digite a matrícula do estudante que deseja excluir: ")
        for p in pessoas:
                pessoas.remove(p)
                print(f"Estudante com matrícula {matricula_excluir} excluído com sucesso!")
                break
        else:
            print(f"Estudante com matrícula {matricula_excluir} não encontrado.")

    elif opcao == 10:
        matricula_excluir = input("Digite a matrícula do professor que deseja excluir: ")
        for p in pessoas:
                pessoas.remove(p)
                print(f"Professor com matrícula {matricula_excluir} excluído com sucesso!")
                break
        else:
            print(f"Professor com matrícula {matricula_excluir} não encontrado.")

    elif opcao == 0:
        print("Saindo do programa...")
        break