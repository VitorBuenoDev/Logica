print("Bem-vindo ao programa =)")


pretende = float(input("Qual quantia você deseja sacar ou depositar? "))

class ContaBancaria:
    def __init__(self, titular, saldo):  
        self.titular = titular
        self.__saldo = saldo
        
    def Sacar(self, quantia):
        if self.__saldo < quantia:
            print("Saldo insuficiente")
        else:
            self.__saldo -= quantia
            print(f"O usuário {self.titular} sacou uma quantia de R${quantia:.2f} e sobraram R${self.__saldo:.2f} na conta.")
        
    def Depositar(self, quantia):
        self.__saldo += quantia
        print(f"O usuário {self.titular} depositou R${quantia:.2f} e ficou com uma quantia de R${self.__saldo:.2f}")

conta = ContaBancaria("José", 125)

cleiton = int(input("Digite 1 para sacar dinheiro e 2 para depositar: "))
if cleiton == 1:
    conta.Sacar(pretende)
elif cleiton == 2:
    quantia_deposito = float(input("Qual quantia você deseja depositar? "))
    conta.Depositar(quantia_deposito)
else:
    print("Opção inválida.")