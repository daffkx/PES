#Lista 1, Exercício 3
nome=(input("Digite o nome de usuário: "))
senha=(input("Digite a senha: "))
if nome=="admin" and senha=="12345":
    print("Login bem-sucedido.")
else:
    print("Nome de usuário ou senha incorretos.")