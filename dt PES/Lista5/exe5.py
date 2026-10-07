#Lista 5, Exercício 5

def lista_vazia(lista):
    return len(lista) == 0

def maior_valor(lista):
    if lista_vazia(lista):
        return -1
    return max(lista)

def menor_valor(lista):
    if lista_vazia(lista):
        return -1
    return min(lista)

def media_valores(lista):
    if lista_vazia(lista):
        return -1
    return sum(lista) / len(lista)

lista1 = []
lista2 = [10, 20, 30, 40, 50]

print("=== TESTE COM LISTA VAZIA ===")
print("Lista:", lista1)
print("Está vazia?", lista_vazia(lista1))
print("Maior valor:", maior_valor(lista1))
print("Menor valor:", menor_valor(lista1))
print("Média:", media_valores(lista1))

print("\n=== TESTE COM LISTA COM ELEMENTOS ===")
print("Lista:", lista2)
print("Está vazia?", lista_vazia(lista2))
print("Maior valor:", maior_valor(lista2))
print("Menor valor:", menor_valor(lista2))
print("Média:", media_valores(lista2))