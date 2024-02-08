from pessoas.pessoa import Pessoa
class Usuario(Pessoa):
    def __init__(self, nome, telefone, nacionalidade):
        self.nome = nome
        self.telefone = telefone
        self.nacionalidade = nacionalidade

user1 = Usuario('23658', 'Karol', '23659874', 'Brasileira')
print('id:', user1.id)
print('Nome:', user1.nome)
print('Telefone:', user1.telefone)
print('Nacionalidade:', user1.nacionalidade)
