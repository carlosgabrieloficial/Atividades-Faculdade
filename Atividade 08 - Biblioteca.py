

class Livro :

    def __init__(self,titulo,autor,ano):

        self.titulo = titulo
        self.autor = autor
        self.ano = ano 
        pass

    def __str__(self):
        return f"{self.titulo} escrito por {self.autor},No ano {self.ano}"
    


    biblioteca = []

    def adicionar_livro(titulo,autor,ano):
        novo_livro = Livro(titulo,autor,ano)
        biblioteca.append(novo_livro)

        print(f"{titulo} foi adiciondo")

    def listar_livro ():
        print()
        for livro in biblioteca:
            print(livro)

adicionar_livro("A","wi" , 1605)



    