from biblioteca.livraria import Biblioteca



def mostrar_menu():
    print("\nBiblioteca Sistema de Gerenciamento")
    print("1 - Adicionar Usuário")
    print("2 - Adicionar Livro")
    print("3 - Emprestar Livro")
    print("4 - Devolver Livro")
    print("5 - Atualizar Usuário")
    print("6 - Remover Livro")
    print("7 - Listas Usuários")
    print("8 - Listar Autores")
    print("9 - Listar livros disponíveis")
    print("10 - Listar livros emprestados")    
    print("0 - Sair")
    escolha = input("Escolha uma opção: ")
    return escolha





def main():
    biblioteca = Biblioteca()
   

    while True:
        escolha = mostrar_menu()
        if escolha == "1":           
            nome = input("Nome do usuário: ")
            telefone = input("Telefone do usuário: ")
            nacionalidade = input("Nacionalidade do usuário: ")
            biblioteca.adicionar_usuario(nome, telefone, nacionalidade)
        elif escolha == "2":
            titulo = input("Título do livro: ")
            autor = input("Autor do livro: ")
            genero = input("Gênero do livro: ")
            quantidade_disponivel = int(input("Quantidade disponível do livro: "))
            maximo_renovacoes = int(input("Máximo de renovações permitidas: "))
            biblioteca.adicionar_livro(titulo, autor, genero, quantidade_disponivel, maximo_renovacoes)
        elif escolha == "3":
            titulo = input("Título do livro que deseja emprestar: ")
            biblioteca.emprestar_livro(titulo)
        elif escolha == "4":
            titulo = input("Título do livro que deseja devolver: ")
            biblioteca.devolver_livro(titulo)
        elif escolha == "5":
            nome_antigo = input("Nome do usuário que deseja atualizar: ")
            novo_nome = input("Novo nome do usuário: ")
            novo_telefone = input("Novo telefone do usuário: ")
            nova_nacionalidade = input("Nova nacionalidade do usuário: ")
            biblioteca.atualizar_usuario(nome_antigo, novo_nome, novo_telefone, nova_nacionalidade)
        elif escolha == "6":
            titulo = input("Título do livro que deseja remover: ")
            biblioteca.remover_livro(titulo)    
        elif escolha == "7":
            biblioteca.listar_usuarios()
        elif escolha == "8":
            biblioteca.listar_autores()
        elif escolha == "9":
            biblioteca.listar_livros()
        elif escolha == "10":
            biblioteca.listar_livros_emprestados()
        elif escolha == "0":
            print("Saindo do sistema...")
            break    
        else:
            print("Opção inválida. Tente novamente.")

       

if __name__ == "__main__":
    main()