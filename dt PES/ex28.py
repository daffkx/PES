#Lista 4, Exercício 3
notas = []

quantidade = int(input("Digite a quantidade de notas: "))

for i in range(quantidade):
    nota = int(input("Digite a nota: "))
    notas.append(nota)

i = 0
while i < len(notas):           #WHILE
    print(f"Nota: {notas[i]}")
    i += 1

#for nota in notas:             #FOR
#   print(f"Nota: {nota}")