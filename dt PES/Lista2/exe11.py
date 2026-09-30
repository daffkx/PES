#Lista 2, Exercício 11
produtos = {
    1: ("Suco", 6.00),
    2: ("Pão de queijo", 3.00),
    3: ("Pastel", 7.00),
    4: ("Salada de frutas", 9.00),
    5: ("Café com Leite", 3.50),
    6: ("Cappuccino", 4.50),
    7: ("Iogurte", 6.50),
    8: ("Água", 2.50)
}

caixa_total = 0

print("=== Cantina ===")
print("Menu de produtos:")
for codigo, (nome, preco) in produtos.items():
    print(f"{codigo} - {nome} (R$ {preco:.2f})")

while True:
    codigo = (int(input("\nDigite o código do produto (Digite 0 para sair): ")))
    if codigo == 0:
        break

    if codigo in produtos:
        quantidade = (int(input("Digite a quantidade: ")))
        nome, preco = produtos[codigo]
        valor_compra = quantidade * preco
        caixa_total += valor_compra
        print(f"\nVocê comprou {quantidade}x {nome}. Total: R$ {valor_compra:.2f}")
    else:
        print("\nCódigo inválido. Tente Novamente.")

print(f"\nValor total acumulado no caixa é de: {caixa_total:.2f}")