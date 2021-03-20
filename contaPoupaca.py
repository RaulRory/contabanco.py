from conta import Conta

class ContaPoupança(Conta):

    def __init__(self, saldo, numeroConta, nome, salario):
        self.criarContaPoupança = {}


    def criarContaPoupança(self, numero, saldo, salario, nome):
        conta = ContaPoupança()
        conta.numeroConta = int(input(print("Digite um numero para a sua conta")))
        conta.saldo = 0
        conta.salario = float(input(print("Qual o seu salario?")))
        conta.nome = input(print("Como você se chama?"))

        listaContas.append(conta)

        print(listaContas)

    def receberSalario(self):
        salario = int(input(print("Quanto você ganha de salario")))
        return salario

    def apagarConta(self, numeroConta):
        listaContas.excluir(numeroConta)

    def alterarConta(self, numeroConta, obejetoAlterado):
        listaContas.Ediar(numeroConta, alteracao)

    def investir(self):
        listContas(investirDinheiro)
