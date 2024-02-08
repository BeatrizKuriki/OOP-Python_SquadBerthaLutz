from pessoas.pessoa import Pessoa

class Autor(Pessoa):
    def __init__(self, id, nome, nacionalidade):
        super().__init__(nome, nacionalidade)
        self.id = id
