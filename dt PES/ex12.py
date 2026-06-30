#Lista 2, Exercício 5
numero = (int(input("Digite um número: ")))

print(f"\nTabuada do número {numero}")
for i in range (1,11):
    resultado = numero * i 
    print(f"\n{numero} x {i} = {resultado}")