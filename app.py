from biblioteca import Biblioteca
import sqlite3


def mostrar_menu():
    print("\nBiblioteca Sistema de Gerenciamento")
    print("1 - Adicionar Usuário")
    print("2 - Adicionar Livro")
    print("3 - Emprestar Livro")
    print("4 - Devolver Livro")
    print("5 - Atualizar Usuário")
    print("6 - Remover Livro")
    print("0 - Sair")
    escolha = input("Escolha uma opção: ")
    return escolha

def main():
    biblioteca = Biblioteca()
    # Se necessário, inicialize o banco de dados ou qualquer configuração inicial aqui

    while True:
        escolha = mostrar_menu()
        if escolha == "1":
            # Lógica para adicionar usuário, por exemplo:
            nome = input("Nome do usuário: ")
            telefone = input("Telefone do usuário: ")
            nacionalidade = input("Nacionalidade do usuário: ")
            # biblioteca.adicionar_usuario(nome, telefone, nacionalidade)
            # Ou diretamente uma função que insere no banco de dados
        elif escolha == "0":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")
        # Implemente as demais opções de forma similar

if __name__ == "__main__":
    main()