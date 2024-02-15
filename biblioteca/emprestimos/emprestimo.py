class Emprestimo:
    def __init__(self, exemplar, usuario, data_emprestimo):
        self.exemplar = exemplar
        self.usuario = usuario
        self.data_emprestimo = data_emprestimo
        self.data_devolucao = None
        self.estado = 'emprestado'

    def detalhes(self):
        return f"Exemplar: {self.exemplar}, Usuário: {self.usuario}, Data de Empréstimo: {self.data_emprestimo}, Estado: {self.estado}"
