#Lista 4, Exercício 6
notas = []

while True:
    print("""
        Notas
        ---------
        [1] - Cadastrar
        [2] - Excluir
        [3] - Listar
        [4] - Calcular média
        [0] - Sair
        ----------
    """)

    opcao = int(input("Digite sua opção: "))

    if opcao == 0:
        print("Encerrando programa.")
        break

    if opcao == 1:
        nota = float(input("Digite a nota que deseja cadastrar: "))
        notas.append(nota)
        print("Nota cadastrada com sucesso!")

    elif opcao == 2:
        if len(notas) == 0:
            print("Não há notas cadastradas para excluir.") 
        else:
            print("Notas cadastradas:")
            for i in range(len(notas)):
                print(f"{i} - {notas[i]}")
            indice = int(input("Digite o índice da nota a excluir: "))
            if 0 <= indice < len(notas):
                removida = notas.pop(indice)
                print(f"Nota {removida} removida com sucesso!")
            else:
                print("Índice inválido.")

    elif opcao == 3:
        if len(notas) == 0:
            print("Não há notas cadastradas.")
        else:
            print("Notas cadastradas:")
            for i in range(len(notas)):
                print(f"{i} - {notas[i]}")

    elif opcao == 4:
        if len(notas) == 0:
            print("Não há notas cadastradas para calcular a média.")
        else:
            soma = 0 
            for nota in notas:
                soma += nota
            media = soma / len(notas)
            print(f"A média das notas cadastradas é: {media:.2f}")

            if media >= 6:
                print("Aprovado!")
            else: 
                print("Reprovado!")