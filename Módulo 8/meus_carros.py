# Meus carros 😌
carro1 = Carro("Chevrolet", "Camaro")
carro2 = CarroEletrico("Tesla", "Model 3", 550)

# Exibindo
carro1.exibir_info()
carro2.exibir_info()

print(carro1)
print(carro2)


# Classe Livro
class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

    def __str__(self):
        status = "Disponível" if self.disponivel else "Emprestado"
        return f"{self.titulo} - {self.autor} ({status})"


# Classe Biblioteca
class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def listar_livros(self):
        print("\n📚 Lista de livros:")
        for livro in self.livros:
            print(livro)

    def emprestar_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo and livro.disponivel:
                livro.disponivel = False
                print(f"\nLivro '{titulo}' emprestado com sucesso!")
                return
        print(f"\nLivro '{titulo}' não disponível.")

    def devolver_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo and not livro.disponivel:
                livro.disponivel = True
                print(f"\nLivro '{titulo}' devolvido com sucesso!")
                return
        print(f"\nLivro '{titulo}' não foi encontrado ou já está disponível.")


# Testando o sistema
biblioteca = Biblioteca()

# Criando livros
livro1 = Livro("É Assim Que Acaba", "Colleen Hoover")
livro2 = Livro("Love & Gelato", "Jenna Evans Welch")

# Adicionando livros
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)

# Listar livros
biblioteca.listar_livros()

# Emprestar livro
biblioteca.emprestar_livro("Love & Gelato")

# Listar novamente
biblioteca.listar_livros()

# Devolver livro
biblioteca.devolver_livro("Love & Gelato")

# Lista final
biblioteca.listar_livros()