#Lista 4, Exercício 4
cidades = []

quantidade = int(input("Digite a quantidade de cidades: "))

for i in range(quantidade):
    cidade = str(input("Digite a cidade: "))
    cidades.append(cidade)

print("\nListando cidades: ")
print(cidades)

excluir = str(input("\nDigite uma cidade a ser excluída: "))

if excluir in cidades:
    indice = cidades.index(excluir)  #index = é a posição do elemento na lista
    cidades.pop(indice)  #pop = remove o elemento da lista
    print("Cidade excluída com sucesso!")
else:
    print("Cidade não encontrada.")

print("\nListando cidades: ")
print(cidades)