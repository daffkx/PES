quantidade = 0 
soma = 0 

while True:
    numero = (int(input("Digite um múmero inteiro (0 para sair): ")))
    if numero == 0:
        break
    quantidade = quantidade + 1  #ou quantidade += 1
    soma = soma + numero  #ou soma += numero

if quantidade > 0:
    media = soma / quantidade
    print(f"\nQuantidade de números digitados: {quantidade}")
    print(f"\nSoma dos números: {soma}")
    print(f"\nMédia aritmética: {media:.2f}")
else:
    print("\nNenhum número foi digitado")
