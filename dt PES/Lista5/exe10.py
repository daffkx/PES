#Lista 5, Exercício 10

import random

def embaralhar_texto(texto):
    texto = texto.lower() 

    lista_caracteres = list(texto)
    random.shuffle(lista_caracteres)

    return "".join(lista_caracteres)

palavra = input("Digite uma palavra ou frase: ")

resultado = embaralhar_texto(palavra)

print("Texto original:", palavra)
print("Texto embaralhado:", resultado)
