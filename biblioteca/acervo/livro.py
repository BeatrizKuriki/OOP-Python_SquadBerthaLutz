from ..pessoas import Autor
from acervo.exemplar import Exemplar

class Livro(Exemplar):
    def __init__(self, titulo, autor, genero, quantidade_total, maximo_renovacoes):     
        super().__init__()  
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.quantidade_total = quantidade_total  
        self.quantidade_disponivel = quantidade_total  
        self.maximo_renovacoes = maximo_renovacoes
        self.autores = []
        self.exemplares = []  

    def adicionar_autor(self, autor):
        self.autores.append(autor)

    def adicionar_exemplar(self, exemplar):
        self.exemplares.append(exemplar)    

    def emprestar_exemplar(self):
        if self.quantidade_disponivel > 0:
            self.quantidade_disponivel -= 1
            return True
        else:
            return False
        
    def devolver_exemplar(self):
        self.quantidade_disponivel += 1

    def realizar_renovacao(self):
        if self.maximo_renovacoes > 0:
            self.maximo_renovacoes -= 1
            return True
        else:
            return False

    @property
    def renovacoes_maximas(self):
        return self.maximo_renovacoes

    def definir_maximo_renovacoes(self, novo_maximo):
        if novo_maximo >= 0:
            self.maximo_renovacoes = novo_maximo
            return True
        else:
            return False
