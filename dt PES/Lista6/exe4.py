#Lista 6, Exercício 4

class produto: 
    def __init__(self, nome, quantidade):
        self.nome = nome
        self.quantidade = quantidade

    def esta_disponivel(self):
        if self.quantidade > 0:
            return True
        else:
            return False
        
    def vernder(self):
        self.quantidade = self.quantidade - 1

produto1 = produto("Guitarra", 800)

print(produto1.esta_disponivel())

produto1.vernder()
produto1.vernder()

print(produto1.esta_disponivel())