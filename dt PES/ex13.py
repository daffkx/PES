numero = (int(input("Digite um número: ")))
inicio = (int(input("Digite o número inicial: ")))
fim = (int(input("Digite o número final: ")))

print(f"\nTabuada do número {numero}")
for i in range (inicio, fim + 1):  #adicionei +1 porque o range não conta o último número   
    resultado = numero * i 
    print(f"\n{numero} x {i} = {resultado}")