from abc import ABC, abstractmethod

class Pessoa(ABC):
     proximo_id = 1
     def __init__(self, nome, telefone, nacionalidade):
        self._id = Pessoa.proximo_id
        self._nome = nome
        self._telefone = telefone
        self._nacionalidade = nacionalidade
        Pessoa.proximo_id +=1


   
    