from ..pessoas import Autor

class Livro:
    def __init__(self, titulo, editora, generos, exemplares_disponiveis, renovacoes_maximas):
        self.titulo = titulo
        self.editora = editora
        self.generos = generos
        self.exemplares_disponiveis = exemplares_disponiveis
        self._renovacoes_maximas = renovacoes_maximas
        self.autores = []

def adicionar_autor(self, autor):
        self.autores.append(autor)

def emprestar_exemplar(self):
        if self.exemplares_disponiveis > 0:
            self.exemplares_disponiveis -= 1
            return True
        else:
            return False
        
def devolver_exemplar(self):
        self.exemplares_disponiveis += 1

def realizar_renovacao(self):
        if self._renovacoes_maximas > 0:
            self._renovacoes_maximas -= 1
            return True
        else:
            return False

@property
def renovacoes_maximas(self):
    return self._renovacoes_maximas

def definir_maximo_renovacoes(self, novo_maximo):
        self._renovacoes_maximas = novo_maximo