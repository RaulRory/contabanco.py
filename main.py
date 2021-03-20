from contaSalario import *
from ContaEspecial import *
from contaPoupaca import *



contador = 1

listaContaSalario = []
listaContaEspecial = []
listaPoupanca = []




while contador > 0:

        opcSalario = int(input(print("Digite: \n"
                                     "1 - Criar uma conta salário \n"
                                     "2 - Tirar um extrato \n"
                                     "3 - Efetuar um saque \n"
                                     "4 - Efetuar um deposito \n")))

        if opcSalario == 1:
            salario = ContaSalario()
            salario.criarContaSalario()

        elif opcSalario == 2:
            salario = ContaSalario()
            salario.extrato()

        elif opcSalario == 3:
            salario = ContaSalario()
            salario.saque()

        elif opcSalario == 4:
            ContaSalario.deposito()





    # if opc == 2:
    #
    #     opcPoupanca = int(input(print("Digite: \n"
    #                                   "1 - Criar uma conta salário \n"
    #                                   "2 - Tirar um extrato \n"
    #                                   "3 - Efetuar um saque \n"
    #                                   "4 - Efetuar um deposito \n"
    #                                   "5 - investir na popança \n")))
    #
    #     if opcPoupanca == 1:
    #         ContaPoupança.criarContaSalario()
    #
    #
    #     elif opcPoupanca == 2:
    #         salario = ContaPoupança.extrato()
    #
    #     elif opcPoupanca == 3:
    #         ContaPoupança.saque()
    #
    #     elif opcPoupanca == 4:
    #         ContaPoupança.deposito()
    #
    #     elif opcPoupanca == 5:
    #         ContaPoupança.investir()
    #
    #
    #
    #
    # if opc == 1:
    #
    #     opcEspecial = int(input(print("Digite: \n"
    #                                   "1 - Criar uma conta salário \n"
    #                                   "2 - Tirar um extrato \n"
    #                                   "3 - Efetuar um saque \n"
    #                                   "4 - Efetuar um deposito \n"
    #                                   "5 - Receber credito \n")))
    #
    #     if opcSalario == 1:
    #         salario = ContaSalario()
    #         salario.criarContaSalario()
    #
    #
    #     elif opcEspecial == 2:
    #         salario = ContaSalario()
    #         salario.extrato()
    #
    #     elif opcEspecial == 3:
    #         contaEspecial.saque()
    #
    #     elif opcEspecial == 4:
    #         contaEspecial.deposito()
    #
    #     elif opcEspecial == 5:
    #         contaEspecial.receberCredito()





