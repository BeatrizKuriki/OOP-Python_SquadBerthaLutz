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

    def adicionar_usuario(self, nome, telefone, nacionalidade):
        novo_usuario = Usuario(nome, telefone, nacionalidade=nacionalidade)
        self.usuarios.append(novo_usuario)
        print("Usuário adicionado com sucesso.")

    def adicionar_livro(self, titulo, autor, genero, quantidade_disponivel, maximo_renovacoes):
        novo_livro = Livro(titulo, autor, genero, quantidade_disponivel, maximo_renovacoes)
        self.livros.append(novo_livro)    

    def emprestar_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo:
                if livro.quantidade_disponivel > 0:
                    livro.quantidade_disponivel -= 1
                    print("Livro emprestado com sucesso.")
                    return
                else:
                    print("Não há exemplares disponíveis para empréstimo.")
                    return
        print("Livro não encontrado.")

    def devolver_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo:
                livro.quantidade_disponivel += 1
                print("Livro devolvido com sucesso.")
                return
        print("Livro não encontrado.")

    def atualizar_usuario(self, nome_antigo, novo_nome, novo_telefone, nova_nacionalidade):
        for usuario in self.usuarios:
            if usuario.nome == nome_antigo:
                usuario.nome = novo_nome
                usuario.telefone = novo_telefone
                usuario.nacionalidade = nova_nacionalidade
                print("Usuário atualizado com sucesso.")
                return
        print("Usuário não encontrado.")

    def remover_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo:
                self.livros.remove(livro)
                print("Livro removido com sucesso.")
                return
        print("Livro não encontrado.")

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
                print(f"Nome: {usuario.nome}, Telefone: {usuario.telefone}, Nacionalidade: {usuario.nacionalidade}")

    def listar_autores(self):
        autores = set(autor for livro in self.livros for autor in livro.autores)
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

    
    def listar_livros(self):
        if not self.livros:
            print("Não há livros cadastrados.")
        else:
            print("Lista de Livros:")
        for livro in self.livros:
            autores = ', '.join(livro.autores)
            print(f"Título: {livro.titulo}, Autores: {autores}, Gênero: {livro.genero}, Quantidade Disponível: {livro.quantidade_disponivel}, Quantidade Total: {livro.quantidade_total}, Máximo de Renovações: {livro.maximo_renovacoes}")

