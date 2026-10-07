#Lista 5, Exercício 7

def desenha_moldura(linhas=1, colunas=1):

    linhas = max(1, min(linhas, 20))
    colunas = max(1, min(colunas, 20))

    print("+" + "-" * colunas + "+")

    for i in range(linhas):
        print("|" + " " * colunas + "|")

    print("+" + "-" * colunas + "+")

linhas = int(input("Digite o número de linhas: "))
colunas = int(input("Digite o número de colunas: "))

desenha_moldura(linhas, colunas)