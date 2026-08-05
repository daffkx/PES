#Lista 3, Exercício 5

nomes = []
idades = []
alturas = []
pesos = []

while True: 
    print("1 - Cadastrar")
    print("2 - Excluir")
    print("3 - Alterar")
    print("4 - Listar")
    print("0 - Sair")

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