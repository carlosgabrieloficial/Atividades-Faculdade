
class Veiculo:

    def __init__(self,Marca,Modelo,Ano):

        self.Marca = Marca
        self.Modelo = Modelo
        self.Ano = Ano
        self.velocidade = 0
        pass

    def aceleracao (self,incremento):
        self.velocidade += incremento

    def frenagem (self,descremento):
        self.velocidade -= descremento

    def status (self):
        return(f"Marca {self.Marca}, modelo {self.Modelo}, ano {self.Ano}, velocidade {self.velocidade}")

class Carro(Veiculo):
    def __init__(self, Marca, Modelo, Ano,potencia):
        super().__init__(Marca, Modelo, Ano)
        self.potencia = potencia

def acelerar (self,incremento):
    self.velocidade += incremento + self.potencia

class Bicicleta (Veiculo):
    def __init__(self, Marca, Modelo, Ano,tipo):
        super().__init__(Marca, Modelo, Ano)
        self.tipo = tipo

    def status (self):
        def status(self):
            return(f"marca{self.Marca}, modelo{self.Modelo}, ano {self.Ano}, tipo{self.tipo}, velocidade {self.velocidade}")

carro01 = Carro("Toyota","Corolla",2023,120)
bicicleta01 = Bicicleta("Trek","BMX",2023,"MTP")

carro01.aceleracao(50)
bicicleta01.aceleracao(10)

print("Status carro")
print(f"{carro01.status()}")
