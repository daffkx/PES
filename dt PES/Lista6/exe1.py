#Lista 6, Exercício 1

class livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def descricao(self):
        return f"{self.titulo} foi escrito por {self.autor}"

livro1 = livro("A história de Dema", "Tyler Joseph")

print(livro1.descricao())