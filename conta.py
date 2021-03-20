


class Conta:

    def __init__(self, nome, numeroConta, saldo=0):
        self.saldo = saldo
        self.numeroConta = numeroConta
        self.nome = nome


    def extrato(self):
        print("Numero da conta: ", self.numeroConta, " Saldo: ", self.saldo)


    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print("você retirou R$ ", valor)


    def deposito(self, valor):
        self.saldo += valor
        print("você depositou R$ ", valor)

# c1=Conta ( 123 , 100)
# 
# c1.extrato()
# 
# c1.deposito(200)
# 
# c1.extrato()
# 
# c1.saque(10)
# 
# c1.extrato()