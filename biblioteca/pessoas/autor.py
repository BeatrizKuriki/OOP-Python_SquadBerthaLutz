from pessoas.pessoa import Pessoa

class Autor(Pessoa):
    def __init__(self, nome, nacionalidade):
        super().__init__(nome, nacionalidade)