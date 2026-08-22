#Lista 5, Exercício 4

def soma(numeros):
    return sum(numeros) 

numeros = [] 

for i in range(4):
    numero = float(input(f"Digite um número: "))
    numeros.append(numero)

resultado = soma(numeros)
print("A soma dos números é:",resultado)