#Lista 6, Exercício 4

class produto: 
    def __init__(self, nome, quantidade):
        self.nome = nome
        self.quantidade = quantidade

    def esta_disponivel(self):
        return self.quantidade > 0

    def vender(self):
        self.quantidade -= 1

produto1 = produto("Guitarra", 4)

produto1.vender()

print(produto1.esta_disponivel())
print(f"Quantidade disponível: {produto1.quantidade}")