from abc import ABC, abstractmethod
class Exemplar(ABC):
    def __init__(self, livro, identificador):
        self.livro = livro  
        self.identificador = identificador  


    @abstractmethod
    def exibir_detalhes(self):
        pass    
