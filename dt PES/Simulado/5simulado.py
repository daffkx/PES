num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

while True:
    print(""" 
        1 - Adição 
        2 - Subtração
        3 - Multiplicação
        4 - Divisão
        0 - Sair    
    """)

    opcao = int(input("Digite a opção desejada: "))
    
    if opcao == 0:
        print("Encerrando programa")
        break

    elif opcao == 1:
        resultado = num1 + num2
        print(f"O resultado da adição é: {resultado}")

    elif opcao == 2:
        resultado = num1 - num2
        print(f"O resultado da subtração é: {resultado}")

    elif opcao == 3:
        resultado = num1 * num2
        print(f"O resultado da multiplicação é: {resultado}")

    elif opcao == 4:
        if num2 != 0:  
            resultado = num1 / num2
            print(f"O resultado da divisão é: {resultado}")
        else:
            print("Erro")

    else:
        print("Erro")

# ===========================================

# def adicao(n1, n2):
# 	resultado = n1 + n2
# 	return resultado

# def subtracao(n1, n2):
# 	resultado = n1 - n2
# 	return resultado

# def multiplicacao(n1, n2):
# 	resultado = n1* n2
# 	return resultado

# def divisao(n1, n2):
# 	if n2 == 0:
# 		print("não pode divisão por zero")
# 	else:
# 		resultado = n1 / n2	
# 		return resultado


# n1 = int(input("Digite o primeiro número: "))
# n2 = int(input("Digite o primeiro número: "))

# while True:
# 	print("""Opções: 
# 		1 – Adição;
# 		2 – Subtração;
# 		3 – Multiplicação;
# 		4 – Divisão;
# 		0 – Sair.
#         """)

# 	opcao = int(input("Digite a opção: "))

# 	if opcao == 0:
# 		print("Encerrando programa")
# 		break

# 	if opcao == 1:
# 		resultado = adicao(n1, n2)
# 		print("Resultado: ", resultado)

# 	if opcao == 2:
# 		resultado = subtracao(n1, n2)
# 		print("Resultado: ", resultado)

# 	if opcao == 3:
# 		resultado = multiplicacao(n1, n2)
# 		print("Resultado: ", resultado)

# 	if opcao == 4:
# 		resultado = divisao(n1, n2)
# 		print("Resultado: ", resultado)