from abc import ABC, abstractmethod

class Exemplar(ABC):
    def __init__(self, livro, identificador):
        self.livro = livro
        self.identificador = identificador
        self.disponivel = True 
        self.renovacoes = 0  

    @abstractmethod
    def exibir_detalhes(self):
        pass

    def emprestar(self):
        if self.disponivel:
            self.disponivel = False
            return True
        return False

    def devolver(self):
        if not self.disponivel:
            self.disponivel = True
            self.renovacoes = 0  
            return True
        return False

    def renovar(self):
        if not self.disponivel and self.renovacoes < self.livro.renovacoes_maximas:
            self.renovacoes += 1
            return True
        return False


