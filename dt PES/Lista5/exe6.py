#Lista 5, Exercício 6

def tempo_total(horas, minutos):
    return horas * 60 + minutos

horas = int(input("Digite a quantidade de horas jogadas: "))
minutos = int(input("Digite a quantidade de minutos jogados: "))

total = tempo_total(horas, minutos)

print("Tempo total jogado:", total, "minutos")