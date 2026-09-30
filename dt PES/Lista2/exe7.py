#Lista 2, Exercício 7
quantidade = int(input("Digite a quantidade de notas: "))

soma = 0

for i in range(1, quantidade + 1):
    nota = float(input(f"Digite a nota {i}: "))
    soma += nota  

media = soma / quantidade

print(f"\nMédia final: {media:.2f}") #.2f = mostrar o número com duas casa decimais em formato de ponto flutuante 

if media >= 6:
    print("Aprovado")
else:
    print("Reprovado")