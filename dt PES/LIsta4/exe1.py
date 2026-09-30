#Lista 4, Exercício 1

bairros = ["Centro"]

for i in range(5):
    nome = input(f"Digite o nome do bairro {i+1}: ")
    bairros.append(nome)

print("\nBairros cadastrados:")
for bairro in bairros:
    print(bairro)