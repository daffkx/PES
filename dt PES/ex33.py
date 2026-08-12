#Lista 4.5, Exercício 1
professores = [{}]

def listar_todos_professores():
    indice

opcao = -1

while opcao != 0 
    print("""
        [1] - Professor: adicionar
        [2] - Professor: Alterar
        [3] - Professor: Excluir
        [4] - Professor: Listar
        [0] - Sair
    """)

    opcao = int(input("Digite sua opção: "))

    if opcao == 1:
        cod = input("Qual é o código do professor?")
        nome = input("Qual é o nome do professor?")

        professores.append({
            "cod" : cod,
            "nome" : nome     
        })
    
    elif opcao == 4:
        indice = 0
        while indice < len(professores):
            print("professor: ")