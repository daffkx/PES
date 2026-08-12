#Lista 4, Exercício 5
#5 – Crie um programa que funcionará como um cadastro de Amigos Próximos no
#Instagram. Seu programa deve permitir que amigos sejam cadastrados ou removidos,
#conforme a solicitação do usuário. Também deve ser possível exibir a lista com todos os
#amigos cadastrados, porém, o programa deve avisar o usuário caso a lista esteja vazia.

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
