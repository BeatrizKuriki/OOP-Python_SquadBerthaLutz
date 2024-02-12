from pessoas.pessoa import Pessoa
class Usuario(Pessoa):
    def __init__(self, nome, telefone, nacionalidade):        
        super().__init__(nome, telefone, nacionalidade)
        

