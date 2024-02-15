from abc import ABC, abstractmethod

class Pessoa(ABC):
    proximo_id = 1

    def __init__(self, nome, telefone, nacionalidade):
        self._id = Pessoa.proximo_id
        Pessoa.proximo_id += 1
        self._nome = nome
        self._telefone = telefone
        self._nacionalidade = nacionalidade

    @property
    def id(self):
        return self._id

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor

    @property
    def telefone(self):
        return self._telefone

    @telefone.setter
    def telefone(self, valor):
        self._telefone = valor

    @property
    def nacionalidade(self):
        return self._nacionalidade

    @nacionalidade.setter
    def nacionalidade(self, valor):
        self._nacionalidade = valor
