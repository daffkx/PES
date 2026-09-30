#Lista 4, Exercício 5
cf = []

while True:
    print(""" 
        --CLOSE FRIENDS--
        [1] - Adicionar amigo próximo
        [2] - Remover amigo próximo
        [3] - Listar amigos próximo
        [0] - Sair
        ------------------
    """)
   
    opcao = int(input("Digite uma opção:"))

    if opcao == 0:
        print("Encarrando programa.")
        break

    if opcao == 1:
        nome_add = str(input("Digite o nome do amigo que deseja adicionar: "))
        cf.append(nome_add)
        print("Amigo próximo adicionado com sucesso!")

    elif opcao == 2:
        nome_rem = str(input("Digite o nome do amigo que deseja remover: "))
        if nome_rem in cf:
            cf.remove(nome_rem)
            print("Amigo próximo removido com sucesso!")
        else:
            print("Amigo não encontrado na lista.")

    elif opcao == 3:
        if len(cf) == 0:
            print("A lista de amigos próximos está vazia.")
        else:
            print("Lista de amigos próximos:")
            for amigo in cf:
                print(amigo)