from conta import Conta
from conta_salario import ContaSalario

def main():
    contador  =  1

    while contador > 0:

        opcao = int(input(
            "\n Digite: \n"
            "1 - Criar uma conta \n"
            "2 - Criar uma conta salário \n"
            "3 - Criar uma conta Poupança \n"
            "4 - Criar uma conta Especial \n"
            "5 - Sair do Programa \n"
        ))


        if opcao == 1:

            nome = str(input("Como você se chama ? "))
            numero_conta = int(input("Digite um numero para a sua conta: "))
            saldo = float(input("Qual o valor do saldo inicial da sua conta ? "))

            conta = Conta(nome, numero_conta, saldo)
            conta.menu()

        elif opcao == 2:

            nome = str(input("Como você se chama ? "))
            numero_conta = int(input("Digite um numero para a sua conta: "))
            saldo = float(input("Qual o valor do saldo inicial da sua conta ? "))

            conta_salario = ContaSalario(nome, numero_conta, saldo)
            conta_salario.criarContaSalario()
            conta_salario.menu()

        elif opcao == 3:
            pass

        elif opcao == 4:
            pass
            
        elif opcao == 5:
            contador  =  -1
        
        else:
            print('Caracter Invalido \n Digite um Numero valido pelo menu')

    print('Programa Encerrado, Bye Bye')


if __name__ == "__main__":
    main()

