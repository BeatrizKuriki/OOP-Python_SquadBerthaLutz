from pessoas.pessoa import Pessoa
class Usuario(Pessoa):
    _proximo_id =1
    def __init__(self, nome, telefone, nacionalidade, email=None, senha=None):        
        super().__init__(nome, telefone, nacionalidade)
        self._id = Usuario._proximo_id
        Usuario._proximo_id += 1
        self._email = email
        self._senha = senha

    def get_email(self):
        return self._email

    def set_email(self, email):
        self._email = email

    def get_senha(self):
        return self._senha

    def set_senha(self, senha):
        self._senha = senha

    def atualizar_informacoes(self, nome=None, telefone=None, email=None, senha=None):
        if nome:
            self._nome = nome
        if telefone:
            self._telefone = telefone
        if email:
            self._email = email
        if senha:
            self._senha = senha    
        

