# Importações necessárias
#import matplotlib.pyplot as plt
#from collections import defaultdict

# Classe Livro
class Livro:
    def _init_(self, titulo, autor, genero, quantidade):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.quantidade = quantidade

    def _str_(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Gênero: {self.genero}, Quantidade: {self.quantidade}"

# Lista para armazenar os livros
livros = []

# Função para cadastrar um novo livro
def cadastrar_livro():
    titulo = input("Título do livro: ")
    autor = input("Autor do livro: ")
    genero = input("Gênero do livro: ")
    try:
        quantidade = int(input("Quantidade disponível: "))
    except ValueError:
        print("Quantidade inválida. Use um número inteiro.")
        return

    novo_livro = Livro(titulo, autor, genero, quantidade)
    livros.append(novo_livro)
    print("Livro cadastrado com sucesso!")

# Função para listar todos os livros
def listar_livros():
    if not livros:
        print("Nenhum livro cadastrado.")
        return

    print("\nLista de Livros:")
    for livro in livros:
        print(livro)

# Função para buscar livro pelo título
def buscar_livro_por_titulo():
    titulo_busca = input("Digite o título do livro a buscar: ").lower()
    encontrados = [livro for livro in livros if livro.titulo.lower() == titulo_busca]

    if encontrados:
        for livro in encontrados:
            print(livro)
    else:
        print("Livro não encontrado.")

# Função para gerar gráfico de livros por gênero
#def gerar_grafico_por_genero():
    #if not livros:
    #    print("Nenhum livro cadastrado para gerar o gráfico.")
    #    return

    #genero_contagem = defaultdict(int)

    #for livro in livros:
    #    genero_contagem[livro.genero] += livro.quantidade

    #generos = list(genero_contagem.keys())
    #quantidades = list(genero_contagem.values())

    #plt.figure(figsize=(10, 6))
    #plt.bar(generos, quantidades, color='skyblue')
    #plt.title("Quantidade de Livros por Gênero")
    #plt.xlabel("Gênero")
    #plt.ylabel("Quantidade")
    #plt.xticks(rotation=45)
    #plt.tight_layout()
    #plt.show()

# Menu principal
def menu():
    while True:
        print("\n--- Sistema de Gerenciamento de Livros ---")
        print("1. Cadastrar novo livro")
        print("2. Listar todos os livros")
        print("3. Buscar livro por título")
        print("4. Gerar gráfico de livros por gênero")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            cadastrar_livro()
        elif escolha == '2':
            listar_livros()
        elif escolha == '3':
            buscar_livro_por_titulo()
        #elif escolha == '4':
        #    gerar_grafico_por_genero()
        elif escolha == '5':
            print("Encerrando o sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu