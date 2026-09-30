#Lista 4, Exercício 2
notas = []

quantidade = int(input("Digite a quantidade de notas: "))

for i in range(quantidade):
    nota = int(input("Digite a nota: "))
    notas.append(nota)

print("Listando notas: ")
print(notas)