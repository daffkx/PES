valor = float(input("Digite o preço do produto:  "))
quantidade =  int(input("Digite a quantidade comprada: "))

total = valor * quantidade

if total >= 100:
    desconto =  total *  (10 / 100)
    preco_final = total - desconto
else:
    preco_final = total

print(f"O valor total a ser pago é de: {preco_final}")