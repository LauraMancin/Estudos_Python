import os
import time
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_menu():
    print("\n" + "=" * 40)
    print("         Bem-vindo ao Seu Banco!         ")
    print("=" * 40)
    print("Escolha uma opção:")
    print("1 - Consultar saldo")
    print("2 - Saque")
    print("3 - Sair")


def consultar_saldo(saldo):
    print(f"Seu saldo atual é: R$ {saldo:.2f}")


def realizar_saque(saldo):
    try:
        valor_saque = float(input("Digite o valor do saque: "))
        if valor_saque <= 0:
            print("Erro: O valor do saque deve ser positivo.")
        elif valor_saque > saldo:
            print("Erro: Saldo insuficiente para realizar o saque.")
        else:
            saldo -= valor_saque #saldo = saldo - valor_saque
            print(f"Saque realizado com sucesso! Novo saldo é: R$ {saldo:.2f}")
    except ValueError:
        print("Erro: Digite um valor numérico válido.")
    return saldo


def main():
    saldo = 1000.00
    while True: 
        data_hora_atual = time.strftime("/%d%m%y %H:%M:%S")
        print(f'data e hora atual é {data_hora_atual}')
        limpar_tela()
        exibir_menu()
        opcao = input("Digite o número da opção desejada: ")

        if opcao == "1":
            consultar_saldo(saldo)
            input("\nPressione Enter para continuar...")

        elif opcao == "2":
            saldo = realizar_saque(saldo)
            input("\nPressione Enter para continuar...")

        elif opcao == "3":
            print("\nEncerrando o programa", end="")
            for i in range(5): #mostra 5 pontinhos
                print(".", end="", flush=True) #flush=true força a impressão imediata
                time.sleep(0.5)
            print('\nPrograma encerrado com sucesso!')
            break

        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
            input("\nPressione Enter para continuar...")

    print("\n" + "=" * 50)
    print("    Obrigada por acessar o nosso banco   Tenha um bom dia!         ")
    print("=" * 50)


if __name__ == "__main__":
    main()
