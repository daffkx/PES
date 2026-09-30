#Lista 5, Exercício 1

def media(notas):
    return sum(notas) / len(notas)

notas = [] 

for i in range(3):
    nota = float(input(f"Digite a nota {i+1}: "))
    notas.append(nota)

resultado = media(notas)
print("A média das três notas é:",resultado)