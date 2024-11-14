class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    def exibir_detalhes(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Ano {self.ano}")

#teste
c1 = Carro("Toyota", "Corolla", 2020)
c2 = Carro("Ferrari", "Enzo", 2002)
c1.exibir_detalhes()
c2.exibir_detalhes()