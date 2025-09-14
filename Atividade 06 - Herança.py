

class Animal:

    def __init__(self,nome):
        self.nome = nome

    def barulho(self):
        pass

class cachorro(Animal):
    def barulho (self):
        return("Latir - auau")
    
luna = cachorro("luna")

print(f"{luna.nome} faz {luna.barulho()}")