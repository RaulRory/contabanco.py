from conta import Conta

listaContaSalario = []


class ContaSalario(Conta):

    def init(self, saldo=0, numeroConta=0, nome="", salario=0):
        super().init(saldo, numeroConta, nome)

        self.salario = salario

    def str(self):
        return "Conta:" + str(self.numeroConta) + " Titular:" + self.nome + " Saldo:" + str(self.saldo)

    def __init__(self):
        self.listaContas = []
        self.conta = {}

    def criarContaSalario(self):
        self.conta['numeroConta'] = int(input("Digite um numero para a sua conta"))
        self.conta['salario'] = float(input("Qual o seu salario?"))
        self.conta['nome'] = str(input("Como você se chama?"))

        self.listaContas.append(self.conta)

        print(self.listaContas)

    def extrato(self, ):
        print("Numero da conta: ", self.conta['numeroConta'], " Saldo: ", self.conta['salario'])

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print("você retirou R$ ", valor)

    def deposito(self, valor):
        self.saldo += valor
        print("você depositou R$ ", valor)