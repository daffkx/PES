dicionario = {
    "apelar": "recorrer a uma decisão judicial, pedir ajuda ou proteção em uma situação difícil, ou usar de meios extremos e exagerados",
}

for i in range(4):
	palavra = input("Digite a palavra: ")
	significado = input("Digite o seu significado: ")
	
	dicionario[palavra] = significado

palavra_buscar = input("Digite a palavra que deseja consultar o significado: ")

if palavra_buscar in dicionario:
    print(f"Palavra encontrada, seu significado é: {dicionario[palavra_buscar]}")  
else: 
	print("Palavra não encontrada")

# ===========================================

# dicionario = {
# 	"apelar": "usar de meios extremos ou exagerados"
# }

# for i in range(4):
# 	palavra = str(input("Digite a palavra: "))
# 	significado = str(input("Digite o significado: "))

# 	dicionario[palavra] = significado

# palavra_buscar = str(input("Digite a palavra que deseja buscar: "))

# if palavra_buscar in dicionario:
# 	print(f"Palavra encontrada, seu significado é: {dicionario[palavra_buscar]}")        
# else: 
# 	print("Palavra não encontrada")
