from conta import Conta

class contaEspecial(Conta):

    def __init__(self, saldo, numeroConta, nome, salario):
        super().__init__(saldo, numeroConta, nome)

        self.especial = salario



    def criarContaSalario(self):
        conta = ContaEspecial()

        conta.numeroConta = input("Digite um numero para a sua conta")
        conta.saldo = 0
        conta.salario = input("Qual o seu salario?")
        conta.nome = input("Como você se chama?")

        listaContas.append(conta)

        print(listaContas)

    def receberSalario(self):
        salario = int(input(print("Quanto você ganha de salario")))
        return salario

    def apagarConta(self, numeroConta):
        listaContas.excluir(numeroConta)

    def alterarConta(self, numeroConta, obejetoAlterado):
        listaContas.Ediar(numeroConta, alteracao)

    def receberCredito(self):
        listaContas.append(receberCredito)
