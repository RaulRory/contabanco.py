listaContas = []

class Conta:

    def __init__(self, nome, numeroConta, saldo=0):
        self.saldo = saldo
        self.numeroConta = numeroConta
        self.nome = nome
        self.conta = {}

        self.conta['numeroConta'] = self.numeroConta 
        self.conta['saldo'] =  self.saldo
        self.conta['nome'] = self.nome

        listaContas.append(self.conta)

    def lisatr_contas(self):
        print(listaContas)

    def extrato(self):
        print("Numero da conta: ", self.numeroConta, " Saldo: ", self.saldo)

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print("você retirou R$ ", valor, "Seu salado é de: ", self.saldo)
        else:
            print('Saldo Insuficiente')

    def deposito(self, valor):
        self.saldo += valor
        print("você depositou R$ ", valor, "Seu salado é de: ", self.saldo)

    def apagar_conta(self):

        numero_conta = int(input("Digite o Numero da sua conta: "))
        for index, conta in enumerate(listaContas):
            if ( conta['numeroConta'] == numero_conta ):
                listaContas.pop(index)
                print ("Sua Conta Foi apagada com Sucesso")
                return True
        print('Numero da Conta não foi encontrado')

    def editar_conta(self):

        numero_conta = int(input("Digite o Numero da sua conta: "))
        
        for index, conta in enumerate(listaContas):
            if ( conta['numeroConta'] == numero_conta ):
                self.conta['nome'] = str(input("Digite o nome para qual deseja alterar ?"))
                print ("O Nome da sua conta foi alterado com Sucesso")
                return True

        print('Numero da Conta não foi encontrado')
    
    def menu(self):
        contador  =  1

        while contador > 0:

            opcao = int(input(
                "\n Digite: \n"
                "1 - Extrato da conta \n"
                "2 - Para o saque na conta \n"
                "3 - Para o deposito na conta \n"
                "4 - Listar todas as contas \n"
                "5 - Apagar uma conta \n"
                "6 - Editar uma conta \n"
                "7 - Voltar para o Menu Princiapal \n"
            ))

            if opcao == 1:
                self.extrato()

            elif opcao == 2:
                valor = int(input("Qual valor você deseja sacar ? "))
                self.saque(valor)

            elif opcao == 3:
                valor = int(input("Qual valor você deseja Depositar ? "))
                self.deposito(valor)

            elif opcao == 4:
                self.lisatr_contas()

            elif opcao == 5:
                self.apagar_conta()

            elif opcao == 6:
                self.editar_conta()

            elif opcao == 7:
                contador = -1
            else:
                print('Caracter Invalido \n Digite um Numero valido pelo menu')