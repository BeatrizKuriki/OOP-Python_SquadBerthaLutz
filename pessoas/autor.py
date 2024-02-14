from pessoas.pessoa import Pessoa

class Autor(Pessoa):
    proximo_id = 1

    def __init__(self, nome, nacionalidade):
        super().__init__(nome, nacionalidade)
        self.id = Autor.proximo_id
        Autor.proximo_id += 1
