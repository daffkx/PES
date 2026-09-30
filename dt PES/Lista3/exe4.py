#Lista 3, Exercício 4
produtos = [-1] *10 

while True:
    print("\nMenu")
    print("-------")
    print("1 - Cadastrar")
    print("2 - Listar todos")
    print("0 - Sair")

    opcao = int(input("Digite a opção: "))

    if opcao == 0:
        print("Finalizando sessão.")
        break 
    
    elif opcao == 1: 
        codigo = int(input("Digite o código do produto: "))
    
        if codigo == -1:
            print("Falha.")
        else:
            cadastrado = False
            for i in range(len(produtos)):
                if produtos[i] == -1:   
                    produtos[i] = codigo
                    print("Cadastro realizado!")
                    cadastrado = True
                    break
            if not cadastrado:
                    print("Falha.")

    elif opcao == 2:
        print("\nCódigos cadastrados:")
        for codigo in produtos:
            if codigo != -1:
                print(codigo)

    else:
        print("Opção inválida.")