numero = (int(input("Digite um número: ")))

if numero >= 1:
    for i in range(1, numero + 1):
    
        print(i)
else:
    for i in range(1, numero - 1, -1):
        print(i)