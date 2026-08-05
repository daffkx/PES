#Lista 2, Exercício 12
while True:
    print("\nMenu")
    print("-------")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Divisão")
    print("4 - Multiplicação")
    print("0 - Sair")

    opcao = int(input("Digite a opção: "))

    if opcao == 0:
        print("Desligando calculadora.")
        break

    elif opcao in [1, 2, 3, 4]:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if opcao == 1:
            resultado = num1 + num2
            print(f"Resultado da soma: {resultado}")

        elif opcao == 2:
            resultado = num1 - num2
            print(f"Resultado da subtração: {resultado}")

        elif opcao == 3:
            if num2 != 0:
                resultado = num1 / num2
                print(f"Resultado da divisão: {resultado}")
            else:
                print("Erro: divisão por zero não é permitida.")

        elif opcao == 4:
            resultado = num1 * num2
            print(f"Resultado da multiplicação: {resultado}")

    else:
        print("Opção inválida. Tente novamente.")