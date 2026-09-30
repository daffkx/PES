#Lista 3, Exercício 1
idades = []

while True:
    print("\nMenu")
    print("-------")
    print("1 - Adicionar idade")
    print("2 - Listar idades maiores ou iguais a 16")
    print("0 - Sair")

    opcao = int(input("Digite a opção: "))

    if opcao == 0:
        print("Finalizando sessão.")
        break  

    elif opcao == 1: 
        idade = int(input("Digite a idade: "))
        idades.append(idade)

    elif opcao ==2:
        print(f"Idades maiores ou iguais a 16: ")
        for idade in idades:
            if idade >= 16:
                print(idade)