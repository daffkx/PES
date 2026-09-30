#Lista 3, Exercício 5

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
        nome = str(input("Digite o nome que seja excluído: "))
        if nome in nomes:
            indice = nomes.index(nome)  #index = é a posição do elemento na lista
            nomes.pop(indice)  #pop = remove o elemento da lista
            idades.pop(indice)
            alturas.pop(indice)
            pesos.pop(indice)
            print("Cadastro excluído com sucesso!")
        else:
            print("Nome não encontrado.")

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
            for i in range(len(nomes)):  #len(nomes) = quantidade de elementos na lista
                print(f"Nome: {nomes[i]}, Idade: {idades[i]}, Altura: {alturas[i]}, Peso: {pesos[i]}")

    elif opcao == 0:
        print("Encerrando programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")