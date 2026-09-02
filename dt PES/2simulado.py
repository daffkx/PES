numeros = []

while len(numeros) < 15:
    num = int(input(f"Digite o {len(numeros)+1}º número: "))
    if num < 1 or num > 75:
        print("Não foi possível armazenar. (Só é permitido números entre 1 e 75)")
    elif num in numeros:
        print("Não foi possível armazenar. (Valor repetido)")
    else:
        numeros.append(num)
        print("Número armazenado com sucesso!")

numeros_ordenados = sorted(numeros)
print("Números armazenados em ordem crescente:", numeros_ordenados)

# ===========================================

# bingo = []
# i = 15

# while i >= 0:
# 	numero = int(input("Digite um número: "))
	
# 	if numero >= 1 and numero <=75 and not numero in bingo:
# 		bingo.append(numero)
# 		i = i - 1

# bingo. sort()

# print(bingo)
