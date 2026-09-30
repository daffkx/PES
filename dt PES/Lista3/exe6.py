#Lista 3, Exercício 6

#index = é a posição do elemento na lista
#pop = remove o elemento da lista
#len(nomes) = quantidade de elementos na lista

nomes = []
idades = []
alturas = []
pesos = []

while True: 
    print("\nMenu")
    print("-------")
    print("1 - Cadastrar")
    print("2 - Excluir")
    print("3 - Alterar")
    print("4 - Listar")
    print("5 - Pesquisar")
    print("0 - Sair")
    print("-------")
    
    opcao = int(input("Digite sua opção: "))
   
    if opcao == 0:
        print("Encarrando programa.")
        break

    if opcao == 1:
        nome = str(input("Digite o seu nome: "))
        idade = int(input("Digite a sua idade: "))
        altura = float(input("Digite a sua altura: "))
        peso = float (input("Digite o seu peso: "))

        nomes.append(nome)
        idades.append(idade)
        alturas.append(altura)
        pesos.append(peso)
        print("Cadastro realizado com sucesso!")

    elif opcao == 2:
        print("Excluir cadastro por nome(1) ou por código(2)?")
        opcao_busca = int(input("Digite sua opção:"))

        if opcao_busca == 1:
             nome = str(input("Digite o nome que deseja excluir: "))
             if nome in nomes:
                indice = nomes.index(nome)  
                nomes.pop(indice) 
                idades.pop(indice)
                alturas.pop(indice)
                pesos.pop(indice)
                print("Cadastro excluído com sucesso!")
             else:
                print("Nome não encontrado.")

        elif opcao_busca == 2:
            codigo = int(input("Digite o código que deseja excluir: "))
            if 0 <= codigo < len(nomes):
                nomes.pop(codigo)
                idades.pop(codigo)
                alturas.pop(codigo)
                pesos.pop(codigo)
                print("Cadastro excluído com sucesso!")
            else:
                print("Código não encontrado.")

    elif opcao == 3:
        nome = str(input("Digite o nome que deseja alterar: "))
        if nome in nomes:
            indice = nomes.index(nome)
            idades[indice] = int(input("Digite a nova idade: "))
            alturas[indice] = float(input("Digite a nova altura: "))
            pesos[indice] = float(input("Digite o novo peso: "))
            print("Cadastro alterado com sucesso!")
        else:
            print("Nome não encontrado.")

    elif opcao == 4:
        if len(nomes) == 0:
            print("Nenhum cadastro encontrado.")
        else:
            print("Listagem de cadastros: ")
            for i in range(len(nomes)):  
                print(f"Nome: {nomes[i]}, Idade: {idades[i]}, Altura: {alturas[i]}, Peso: {pesos[i]}")

    elif opcao == 5:
        nome = str(input("Digite o nome que deseja pesquisar: "))
        if nome in nomes:
            indice = nomes.index(nome)
            print(f"Nome: {nomes[indice]}, Idade: {idades[indice]}, Altura: {alturas[indice]}, Peso: {pesos[indice]}")
        else:
            print("Nome não encontrado.")

    elif opcao == 0:
        print("Encerrando programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")