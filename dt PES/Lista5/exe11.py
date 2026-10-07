#Lista 5, Exercício 11

def numero_extenso(n):
    unidades = ["", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"]
    especiais = ["dez", "onze", "doze", "treze", "quatorze", "quinze",
"dezesseis", "dezessete", "dezoito", "dezenove"]
    dezenas = ["", "", "vinte", "trinta", "quarenta", "cinquenta",
"sessenta", "setenta", "oitenta", "noventa"]
    centenas = ["", "cento", "duzentos", "trezentos", "quatrocentos",
"quinhentos", "seiscentos", "setecentos", "oitocentos",
"novecentos"]

    if n == 0:
        return "zero"

    if n == 100:
        return "cem"
    
    texto = ""

    c = n // 100
    d = (n % 100) // 10
    u = n % 10

    if c > 0:
        texto += centenas[c]

    resto = n % 100

    if resto > 0:
        if texto:
            texto += " e "

    if 10 <= resto <= 19:
        texto += especiais[resto - 10]
    else:
        if d > 0:
            texto += dezenas[d]

    if u > 0:
        if d > 0:
            texto += " e "
        texto += unidades[u]

    return texto

def valor_extenso(valor):
    reais = int(valor)
    centavos = round((valor - reais) * 100)

    if reais < 1000:
        texto_reais = numero_extenso(reais)
    else:
        milhar = reais // 1000
        resto = reais % 1000

        texto_reais = numero_extenso(milhar) + " mil"

        if resto > 0:
            texto_reais += " " + numero_extenso(resto)

    if reais == 1:
        texto_reais += " real"
    else:
        texto_reais += " reais"

    if centavos > 0:
        texto_centavos = numero_extenso(centavos)

        if centavos == 1:
            texto_centavos += " centavo"
        else:
            texto_centavos += " centavos"

        return texto_reais + " e " + texto_centavos

    return texto_reais

valor = float(input("Digite um valor em reais: R$ "))
print(valor_extenso(valor))