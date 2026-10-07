#Lista 5, Exercício 9

def data_por_extenso(data):
    dias = [
        "", "primeiro", "dois", "três", "quatro", "cinco", "seis",
        "sete", "oito", "nove", "dez", "onze", "doze", "treze",
        "quatorze", "quinze", "dezesseis", "dezessete", "dezoito",
        "dezenove", "vinte", "vinte e um", "vinte e dois",
        "vinte e três", "vinte e quatro", "vinte e cinco",
        "vinte e seis", "vinte e sete", "vinte e oito",
        "vinte e nove", "trinta", "trinta e um"
    ]

    meses = {
        1: "janeiro",
        2: "fevereiro",
        3: "março",
        4: "abril",
        5: "maio",
        6: "junho",
        7: "julho",
        8: "agosto",
        9: "setembro",
        10: "outubro",
        11: "novembro",
        12: "dezembro"
    }

    anos = {
        2000: "dois mil",
        2001: "dois mil e um",
        2002: "dois mil e dois",
        2003: "dois mil e três",
        2004: "dois mil e quatro",
        2005: "dois mil e cinco",
        2006: "dois mil e seis",
        2007: "dois mil e sete",
        2008: "dois mil e oito",
        2009: "dois mil e nove",
        2010: "dois mil e dez",
        2011: "dois mil e onze",
        2012: "dois mil e doze",
        2013: "dois mil e treze",
        2014: "dois mil e quatorze",
        2015: "dois mil e quinze",
        2016: "dois mil e dezesseis",
        2017: "dois mil e dezessete",
        2018: "dois mil e dezoito",
        2019: "dois mil e dezenove",
        2020: "dois mil e vinte",
        2021: "dois mil e vinte e um",
        2022: "dois mil e vinte e dois",
        2023: "dois mil e vinte e três",
        2024: "dois mil e vinte e quatro",
        2025: "dois mil e vinte e cinco",
        2026: "dois mil e vinte e seis",
        2027: "dois mil e vinte e sete",
        2028: "dois mil e vinte e oito",
        2029: "dois mil e vinte e nove",
        2030: "dois mil e trinta",
        2040: "dois mil e quarenta",
        2050: "dois mil e cinquenta",
        2060: "dois mil e sessenta",
        2070: "dois mil e setenta",
        2080: "dois mil e oitenta",
        2090: "dois mil e noventa",
        2100: "dois mil e cem"
    }

    dia, mes, ano = data.split("/")
    dia = int(dia)
    mes = int(mes)
    ano = int(ano)

    if ano in anos:
        ano_extenso = anos[ano]
    else:
        dezena = (ano // 10) * 10
        unidade = ano % 10
        ano_extenso = anos[dezena] + " e " + dias[unidade]

    return f"{dias[dia]} de {meses[mes]} de {ano_extenso}"

data = input("Digite uma data (DD/MM/AAAA): ")
print(data_por_extenso(data))