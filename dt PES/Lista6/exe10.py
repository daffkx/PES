import pickle

class Estudante:
    def __init__(self, matricula, nome, sobrenome, idade):
        self.tipo = "estudante"
        self.matricula = matricula
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade

    def apresentar(self):
        return f"MATRÍCULA - {self.matricula}, NOME - {self.nome}, SOBRENOME - {self.sobrenome}, IDADE - {self.idade}"


class Professor:
    def __init__(self, matricula, nome, sobrenome, idade, especializacao):
        self.tipo = "professor"
        self.matricula = matricula
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.especializacao = especializacao

    def apresentar(self):
        return f"MATRÍCULA - {self.matricula}, NOME - {self.nome}, SOBRENOME - {self.sobrenome}, IDADE - {self.idade}, ESPECIALIZAÇÃO - {self.especializacao}"


pessoas = []

while True:
    print("\nCadastro de Pessoas")
    print("-------------------")
    print("1 - Cadastrar estudante")
    print("2 - Cadastrar professor")
    print("3 - Listar estudantes")
    print("4 - Listar professores")
    print("5 - Alterar estudante pela matrícula")
    print("6 - Alterar estudante pelo nome")
    print("7 - Alterar professor pela matrícula")
    print("8 - Alterar professor pelo nome")
    print("9 - Excluir estudante pela matrícula")
    print("10 - Excluir professor pela matrícula")
    print("11 - Salvar dados")
    print("12 - Carregar dados")
    print("0 - Sair")

    opcao = int(input("Opção: "))

    if opcao == 1:
        matricula = input("Matrícula: ")
        nome = input("Nome: ")
        sobrenome = input("Sobrenome: ")
        idade = int(input("Idade: "))

        estudante = Estudante(matricula, nome, sobrenome, idade)
        pessoas.append(estudante)

        print("Estudante cadastrado com sucesso!")

    elif opcao == 2:
        matricula = input("Matrícula: ")
        nome = input("Nome: ")
        sobrenome = input("Sobrenome: ")
        idade = int(input("Idade: "))
        especializacao = input("Especialização: ")

        professor = Professor(
            matricula,
            nome,
            sobrenome,
            idade,
            especializacao
        )

        pessoas.append(professor)

        print("Professor cadastrado com sucesso!")

    elif opcao == 3:
        print("\nESTUDANTES:")

        encontrou = False

        for p in pessoas:
            if p.tipo == "estudante":
                print(p.apresentar())
                encontrou = True

        if not encontrou:
            print("Nenhum estudante cadastrado.")

    elif opcao == 4:
        print("\nPROFESSORES:")

        encontrou = False

        for p in pessoas:
            if p.tipo == "professor":
                print(p.apresentar())
                encontrou = True

        if not encontrou:
            print("Nenhum professor cadastrado.")

    elif opcao == 5:
        matricula = input("Digite a matrícula do estudante: ")

        for p in pessoas:
            if p.tipo == "estudante" and p.matricula == matricula:
                p.nome = input("Novo nome: ")
                p.sobrenome = input("Novo sobrenome: ")
                p.idade = int(input("Nova idade: "))

                print("Estudante atualizado com sucesso!")
                break
        else:
            print("Estudante não encontrado.")

    elif opcao == 6:
        nome = input("Digite o nome do estudante: ")

        for p in pessoas:
            if p.tipo == "estudante" and p.nome.lower() == nome.lower():
                p.nome = input("Novo nome: ")
                p.sobrenome = input("Novo sobrenome: ")
                p.idade = int(input("Nova idade: "))

                print("Estudante atualizado com sucesso!")
                break
        else:
            print("Estudante não encontrado.")

    elif opcao == 7:
        matricula = input("Digite a matrícula do professor: ")

        for p in pessoas:
            if p.tipo == "professor" and p.matricula == matricula:
                p.nome = input("Novo nome: ")
                p.sobrenome = input("Novo sobrenome: ")
                p.idade = int(input("Nova idade: "))
                p.especializacao = input("Nova especialização: ")

                print("Professor atualizado com sucesso!")
                break
        else:
            print("Professor não encontrado.")

    elif opcao == 8:
        nome = input("Digite o nome do professor: ")

        for p in pessoas:
            if p.tipo == "professor" and p.nome.lower() == nome.lower():
                p.nome = input("Novo nome: ")
                p.sobrenome = input("Novo sobrenome: ")
                p.idade = int(input("Nova idade: "))
                p.especializacao = input("Nova especialização: ")

                print("Professor atualizado com sucesso!")
                break
        else:
            print("Professor não encontrado.")

    elif opcao == 9:
        matricula = input("Digite a matrícula do estudante: ")

        for p in pessoas:
            if p.tipo == "estudante" and p.matricula == matricula:
                pessoas.remove(p)

                print("Estudante excluído com sucesso!")
                break
        else:
            print("Estudante não encontrado.")

    elif opcao == 10:
        matricula = input("Digite a matrícula do professor: ")

        for p in pessoas:
            if p.tipo == "professor" and p.matricula == matricula:
                pessoas.remove(p)

                print("Professor excluído com sucesso!")
                break
        else:
            print("Professor não encontrado.")

    elif opcao == 11:
        with open("dados_escola.pkl", "wb") as arquivo:
            pickle.dump(pessoas, arquivo)

        print("Dados salvos com sucesso!")

    elif opcao == 12:
        try:
            with open("dados_escola.pkl", "rb") as arquivo:
                pessoas = pickle.load(arquivo)

            print("Dados carregados com sucesso!")

        except FileNotFoundError:
            print("Arquivo não encontrado!")

    elif opcao == 0:
        print("Saindo do programa...")
        break

    else:
        print("Opção inválida!")