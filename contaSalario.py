from conta import Conta

lista_contas_salarios = []

class ContaSalario(Conta):
            
    def __init__(self, nome, numeroConta, saldo):
        super().__init__(nome, numeroConta, saldo)

    def criarContaSalario(self):

        self.conta['salario'] = float(input("Qual o valor vai exportar para sua conta salario ? "))
        self.conta['tipo'] = "Conta Salario"       
        lista_contas_salarios.append(self.conta)

    def lisatr_contas(self):
        print(lista_contas_salarios)
    
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
    
    def depositar_salario_em_conta(self):
        if self.conta['salario'] > 0:
            self.saldo += self.conta['salario']
            print(f"você depositou  R$, {self.conta['salario']} em sua conta, Seu salado é de:  {self.saldo}")
            self.conta['salario'] -= self.conta['salario']
        else:
            print(f"Seu salario no momento é R$, {self.conta['salario']}, Não possivel depositar nenhum valor no momento")

    def apagar_conta(self):

        numero_conta = int(input("Digite o Numero da sua conta: "))
        for index, conta in enumerate(lista_contas_salarios):
            if ( conta['numeroConta'] == numero_conta ):
                lista_contas_salarios.pop(index)
                print ("Sua Conta Foi apagada com Sucesso")
                return True
        print('Numero da Conta não foi encontrado')

    def editar_conta(self):

        numero_conta = int(input("Digite o Numero da sua conta: "))
        
        for index, conta in enumerate(lista_contas_salarios):
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
                "4 - Depositar Salario em conta \n"
                "5 - Listar todas as contas \n"
                "6 - Apagar uma conta \n"
                "7 - Editar uma conta \n"
                "8 - Voltar para o Menu Princiapal \n"
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
                self.depositar_salario_em_conta()

            elif opcao == 5:
                self.lisatr_contas()

            elif opcao == 6:
                self.apagar_conta()

            elif opcao == 7:
                self.editar_conta()

            elif opcao == 8:
                contador = -1
            else:
                print('Caracter Invalido \n Digite um Numero valido pelo menu')
    