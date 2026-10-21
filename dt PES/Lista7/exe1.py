#Lista 7, Exercício 1

class Marcador_de_pagina:
    def __init__(self, pagina_atual):
        self.pagina_atual = pagina_atual

class Livro:
    def __init__(self, titulo, total_paginas):
        self.titulo = titulo
        self.total_paginas = total_paginas
        self.marcador = None 

    def adicionar_marcador(self, pagina):
        if self.marcador is None:
            self.marcador = Marcador_de_pagina(pagina)
        else:
            self.marcador.pagina_atual = pagina 

livro = Livro("A história de Dema", 100)
livro.adicionar_marcador(10)
print(f"Livro: {livro.titulo}, Total de páginas: {livro.total_paginas}, Página atual do marcador: {livro.marcador.pagina_atual}")