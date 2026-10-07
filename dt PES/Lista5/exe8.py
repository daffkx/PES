#Lista 5, Exercício 8

def converter_hora(hora_24):
    horas, minutos = map(int, hora_24.split(":"))

    if horas == 0:
        horas = 12
    periodo = "A"
    if horas < 12:
        periodo = "A"
    elif horas == 12:
        periodo = "P"
    else:
        horas -= 12
        periodo = "P"

    hora_convertida = f"{horas}:{minutos:02d}"
    return hora_convertida, periodo

def imprimir_hora(hora, periodo):
    if periodo == "A":
        print("Hora convertida:", hora, "A.M.")
    else:
        print("Hora convertida:", hora, "P.M.")

while True:
    hora_24 = input("Digite a hora no formato 24h (HH:MM): ")

    hora_convertida, periodo = converter_hora(hora_24)
    imprimir_hora(hora_convertida, periodo)

    continuar = input("Deseja converter outra hora? (S/N): ").upper()

    if continuar != "S":
        print("Programa encerrado.")
        break