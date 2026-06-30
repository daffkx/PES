#Lista 1, Exercício 5
temp=(input("Digite a temperatura em Celsius: "))
temp=float(temp)
if temp<10:
    print("Está muito frio! Use roupas quentes.")
elif temp>=10 and temp<=20:
    print("Frio. Vista-se bem!")
elif temp>20 and temp<=25:
    print("Temperatura agradável. Aproveite o dia!")
elif temp>25 and temp<=30:
    print("Está ficando quente!")
else:
    print("Está muito quente! Use roupas leves e se hidrate.")