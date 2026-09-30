dicionario = {
    "Apelar": "recorrer a uma decisão judicial, pedir ajuda ou proteção em uma situação difícil, ou usar de meios extremos e exagerados",
	"Dafne": "nome próprio feminino de origem grega, é associado à mitologia grega, onde Dafne era uma ninfa transformada em loureiro para escapar do deus Apolo",
	"Patrícia": "nome próprio feminino de origem latina, é associado à mitologia romana, onde Patrícia era uma deusa da agricultura e da fertilidade"
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

# print(dicionario.keys()) #printar as chaves do dicionário
# print(dicionario.values()) #printar os valores do dicionário
# print(dicionario.items()) #printar as chaves e valores do dicionário
# dicionario.pop("Apelar") #remover a chave e o valor do dicionário
# if Apelar in dicionario: #verificar se a chave existe no dicionário
# 	print("Existe")
# else:
# 	print("Não existe")
#print(len(dicionario)) #printar o tamanho do dicionário
#dicionario.sum() #somar os valores do dicionário
#dicionario.append({"Apelar": "usar de meios extremos ou exagerados"}) #adicionar um novo item ao dicionário
#dicionario.get("Apelar") #pegar o valor da chave do dicionário
#dicionario.sort() #ordenar o dicionário
#numeros.sort(reverse=True) #ordenar o dicionário em ordem decrescente

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