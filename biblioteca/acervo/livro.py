class Livro:
    def __init__(self,titulo,editora,generos=None):
        self.titulo = titulo
        self.editora= editora
        self.generos=[]

    def adicionar_genero(self, genero):
        self.generos.append(genero)
