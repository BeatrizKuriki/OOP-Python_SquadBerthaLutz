





class Emprestimo:
    def __init__(self, exemplar, usuario, data_emprestimo, data_devolucao=None):
        self.exemplar = exemplar
        self.usuario = usuario
        self.data_emprestimo = data_emprestimo
        self.data_devolucao = data_devolucao
        self.estado = 'emprestado' if not data_devolucao else 'devolvido'

    def renovar(self):
        if self.exemplar.livro.renovacoes_maximas > 0:
            self.exemplar.livro.renovacoes_maximas -= 1
            self.estado = 'renovado'
            return True
        return False
