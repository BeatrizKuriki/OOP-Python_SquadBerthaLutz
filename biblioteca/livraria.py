from pessoas.usuario import Usuario
from acervo.livro import Livro
from emprestimos.emprestimo import Emprestimo




class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []
        self.emprestimos = []


    def registrar_emprestimo(self, exemplar, usuario, data_emprestimo):
        emprestimo = Emprestimo(exemplar, usuario, data_emprestimo)
        self.emprestimos.append(emprestimo)
        exemplar.disponivel = False
        return emprestimo

    def registrar_devolucao(self, emprestimo, data_devolucao):
        emprestimo.data_devolucao = data_devolucao
        emprestimo.estado = 'devolvido'
        emprestimo.exemplar.disponivel = True    

    def adicionar_usuario(self, nome, telefone, email):
        novo_usuario = Usuario(nome, telefone, email)
        self.usuarios.append(novo_usuario)

    def adicionar_livro(self, titulo, autor, genero, quantidade_disponivel, maximo_renovacoes):
        novo_livro = Livro(titulo, autor, genero, quantidade_disponivel, maximo_renovacoes)
        self.livros.append(novo_livro)    

    def listar_emprestimos(self):
        if not self.emprestimos:
            print("Não há empréstimos registrados.")
        else:
            for emprestimo in self.emprestimos:
                print(f"Empréstimo: {emprestimo.detalhes()}")    

    
    def listar_usuarios(self):
        if not self.usuarios:
            print("Não há usuários cadastrados.")
        else:
            print("Lista de Usuários:")
            for usuario in self.usuarios:
                print(f"Nome: {usuario.nome}, Telefone: {usuario.telefone}, Email: {usuario.email}")

    def listar_autores(self):
        autores = set(livro.autor for livro in self.livros)
        print("Lista de Autores:")
        for autor in autores:
            print(autor)

    def listar_livros_disponiveis(self):
        livros_disponiveis = [livro for livro in self.livros if livro.quantidade_disponivel > 0]
        if not livros_disponiveis:
            print("Não há livros disponíveis.")
        else:
            print("Livros Disponíveis:")
            for livro in livros_disponiveis:
                print(f"Título: {livro.titulo}, Autor: {livro.autor}, Gênero: {livro.genero}")

    def listar_livros_emprestados(self):
        livros_emprestados = [emprestimo.exemplar for emprestimo in self.emprestimos]
        if not livros_emprestados:
            print("Não há livros emprestados.")
        else:
            print("Livros Emprestados:")
            for livro in livros_emprestados:
                print(f"Título: {livro.titulo}, Autor: {livro.autor}, Gênero: {livro.genero}")





