

class Pessoa :

    def __init__(self,nome,idade,genero):

        self.nome = nome
        self.idade = idade
        self.genero = genero
        pass

    def comprimento(self):
        return (f"Ola meu nome é {self.nome}")
    
    def aniversario (self):
        self.idade += 1

pessoa_01 = Pessoa("Joao",30,"Masculino")


print(pessoa_01.comprimento())
print(f"Minha idade é {pessoa_01.idade}")

pessoa_01.aniversario()
print(f"E minha proxima idade é {pessoa_01.idade}")