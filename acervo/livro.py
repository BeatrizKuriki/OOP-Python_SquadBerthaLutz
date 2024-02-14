from pessoas.autor import Autor

class Livro:
    def __init__(self, titulo, editora, generos, exemplares, renovacoes_maximas):
        self.titulo = titulo
        self.editora = editora
        self.generos = generos
        self.exemplares = exemplares
        self._renovacoes_maximas = renovacoes_maximas
        self.autores = []


    def exibir_detalhes(self):
        print(f"Livro: {self.titulo} - Autor: {self.autor} - Gênero: {self.genero}")
    

    def adicionar_autor(self, autor):
        if isinstance(autor, Autor):
            self.autores.append(autor)

    def adicionar_exemplar(self, exemplar):
        self.exemplares.append(exemplar)

   
    def emprestar_exemplar(self):
        for exemplar in self.exemplares:
            if exemplar.disponivel:
                exemplar.emprestar()
                return True
        return False

    
    def devolver_exemplar(self, identificador):
        for exemplar in self.exemplares:
            if exemplar.identificador == identificador and not exemplar.disponivel:
                exemplar.devolver()
                return True
        return False

  
    def realizar_renovacao(self, identificador):
        for exemplar in self.exemplares:
            if exemplar.identificador == identificador and not exemplar.disponivel and self._renovacoes_maximas > 0:
                exemplar.renovar()
                self._renovacoes_maximas -= 1
                return True
        return False

    @property
    def renovacoes_maximas(self):
        return self._renovacoes_maximas

    def definir_maximo_renovacoes(self, novo_maximo):
        if novo_maximo >= 0:
            self._renovacoes_maximas = novo_maximo
            return True
        else:
            return False
