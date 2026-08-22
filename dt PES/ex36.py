#Lista 5, Exercício 2

#usando print

def impar_ou_par(valor):
    if (valor % 2) != 0:
        print("É ímpar")
    else: 
        print("É par")

numero = int(input("Digite um número: "))
impar_ou_par(numero)

# /////////////////////////////////////////

#usando return

#def impar_ou_par(valor):
   #if (valor % 2) != 0:
        #return "É ímpar"
    #else: 
        #return "É par"

#numero = int(input("Digite um número: "))
#resultado = impar_ou_par(numero)
#print(resultado)

# /////////////////////////////////////////

#nível expert

#def eh_digimon_ou_pokemon(nome):
    #if (nome == "metamon"):
        #return "pokemon"

    #if "mon" in nome:
        #return "digimon"
    #else:
        #return "pokemon"

#nome_bicho = input("Digite o nome da criatura: ")
#tipo = eh_digimon_ou_pokemon(nome_bicho)
#if tipo == "pokemon":
    #print("Muito legal o seu monstrinho do pokemon")
    #print("O meu favorito é a lunala")
#else:
    #print("Não sei nada de digimon")