#Lista 4.5, Exercício 1

professores = {
    "001": "Prof Thiago Paes",
    "002": "Prof Schalata",
    "003": "Prof Ignácio",
    "004": "Prof Ryan",
    "005": "Prof André",
    "006": "Profª Fabiana",
    "007": "Prof Alberto",
    "008": "Prof Juliano",
    "009": "Prof Thiago Waltrik",
    "010": "Prof João Eduardo"
}

acessos = {
    "Lab102": ["003", "001", "004", "005", "006"],
    "Lab103": ["007"],
    "Lab104": ["004", "008", "002", "005"],
    "Lab105": ["003", "007", "009", "001"],
    "Lab106": ["002", "003", "009", "001"],
    "Lab107": ["005", "002", "009", "001", "010"]
}

def adicionar_professor():
    codigo = input("Código: ")
    nome = input("Nome: ")
    professores[codigo] = nome
    print("Professor cadastrado com sucesso!")

def alterar_professor():
    codigo = input("Código do professor: ")
    if codigo in professores:
        novo_nome = input("Novo nome: ")
        professores[codigo] = novo_nome
        print("Professor alterado!")
    else:
        print("Professor não encontrado!")

def excluir_professor():
    codigo = input("Código do professor: ")

    if codigo in professores:
        chaves = list(professores.keys())
        chaves.remove(codigo)

    novo = {}
    for c in chaves:
        novo[c] = professores[c]

    professores.clear()
    professores.update(novo)

    for lab in acessos:
        if codigo in acessos[lab]:
            acessos[lab].remove(codigo)
            print("Professor excluído!")
        else:
            print("Professor não encontrado!")

def listar_professores():
    print("\n--- PROFESSORES ---")
    for codigo, nome in professores.items():
        print(codigo, "-", nome)

def adicionar_acesso():
    codigo = input("Código do professor: ")
    laboratorio = input("Laboratório: ")

    if codigo in professores and laboratorio in acessos:
        if codigo not in acessos[laboratorio]:
            acessos[laboratorio].append(codigo)
            print("Acesso cadastrado!")
        else:
            print("Acesso já existe!")
    else:
        print("Professor ou laboratório inválido!")

def alterar_acesso():
    codigo = input("Código do professor: ")
    lab_antigo = input("Laboratório atual: ")
    lab_novo = input("Novo laboratório: ")

    if lab_antigo in acessos and lab_novo in acessos:
        if codigo in acessos[lab_antigo]:
            acessos[lab_antigo].remove(codigo)
            acessos[lab_novo].append(codigo)
            print("Acesso alterado!")
        else:
            print("Professor não possui acesso neste laboratório!")
    else:
        print("Laboratório inválido!")

def excluir_acesso():
    codigo = input("Código do professor: ")
    laboratorio = input("Laboratório: ")

    if laboratorio in acessos and codigo in acessos[laboratorio]:
        acessos[laboratorio].remove(codigo)
        print("Acesso excluído!")
    else:
        print("Acesso não encontrado!")

def listar_acessos():
    print("\n--- ACESSOS ---")

    for laboratorio, lista_codigos in acessos.items():
        print(f"\n{laboratorio}:")
        for codigo in lista_codigos:
            print("-", professores[codigo])

def testar_acesso():
    laboratorio = input("Laboratório: ")
    codigo = input("Código do professor: ")

    if laboratorio in acessos:
        if codigo in acessos[laboratorio]:
            print("ACESSO PERMITIDO")
        else:
            print("ACESSO NEGADO")
    else:
        print("Laboratório inexistente!")

while True:
    print("\n===== SISTEMA DE ACESSO =====")
    print("1 - Adicionar Professor")
    print("2 - Alterar Professor")
    print("3 - Excluir Professor")
    print("4 - Listar Professores")
    print("5 - Adicionar Acesso")
    print("6 - Alterar Acesso")
    print("7 - Excluir Acesso")
    print("8 - Listar Acessos")
    print("9 - Testar Acesso")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_professor()
    elif opcao == "2":
        alterar_professor()
    elif opcao == "3":
        excluir_professor()
    elif opcao == "4":
        listar_professores()
    elif opcao == "5":
        adicionar_acesso()
    elif opcao == "6":
        alterar_acesso()
    elif opcao == "7":
        excluir_acesso()
    elif opcao == "8":
        listar_acessos()
    elif opcao == "9":
        testar_acesso()
    elif opcao == "0":
        print("Sistema encerrado.")
        break
    else:
        print("Opção inválida!")