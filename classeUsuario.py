class Usuario:
    def __init__(self, nome, telefone, nacionalidade):
        self.nome = nome
        self.telefone = telefone
        self.nacionalidade = nacionalidade

user1 = Usuario('Karol', '23659874', 'Brasileira')
print('Nome:', user1.nome)
print('Telefone:', user1.telefone)
print('Nacionalidade:', user1.nacionalidade)