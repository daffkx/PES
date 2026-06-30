#Lista 2, Exercício 8
divida_inicial = float(input("Digite o valor da dívida: "))
meses = int(input("Digite a quantidade de meses: "))
taxa_juros = 0.153  #15,30% ao mês

divida_final = divida_inicial * (1 + taxa_juros) ** meses

print(f"\nApós {meses} meses, sua dívida será de R$ {divida_final:.2f}")