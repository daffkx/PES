deposito = (float(input("Digite o valor que você depositará mensalmente: ")))
meses = (int(input("Digite a quantidade se meses: ")))
taxa_juros = 0.005 #0,5% ao mês

saldo = 0 

print("\nSaldo Final:")
for i in range(1, meses + 1):
    saldo = saldo * (1 + taxa_juros)
    saldo += deposito #abreviação de saldo = saldo + deposito
    print(f"Mês {i}:  R$ {saldo:.2f}")

print(f"\nDepois de {meses} meses, o saldo total será  R$ {saldo:.2f10}")