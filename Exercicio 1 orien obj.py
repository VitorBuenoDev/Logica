class Pessoa:
    def __init__(self, nome, idade):  
        self.nome = nome
        self.idade = idade

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}")


p1 = Pessoa("João", 30)
p2 = Pessoa("Maria", 25)
p1.exibir_informacoes()  
p2.exibir_informacoes()  