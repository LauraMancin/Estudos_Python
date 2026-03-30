import os 

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


# Variáveis globais
saldo = 0.0
extrato = []
compras = {
    'essencial': [],
    'pessoal': [],
    'lazer': [],
    'saude': []
}


def exibir_menu():
    #solicitando ação do cliente
    print('--- MINHAS FINANÇAS ---')    
    print('1- Acessar Saldo')
    print('2- Adicionar Dinheiro')
    print('3- Sacar Dinheiro')
    print('4- Adicionar Compra')
    print('5- Acessar extrato')
    print('6- Sair')
    print('-----------------------')


def acessar_saldo():
    global saldo
    if saldo == 0:
        print('Você não tem saldo!')
    else:
        print(f'Seu saldo é de R$ {saldo:.2f}')

    input('Aperte qualquer tecla para continuar!')


def adicionar_dinheiro():
    global saldo, extrato
    entrada = float(input('Quanto você quer adicionar: '))
    saldo += entrada
    extrato.append(f'Depósito: +R$ {entrada:.2f}')
    print(f'R$ {entrada:.2f} adicionado com sucesso!')
    input('Aperte qualquer tecla para continuar!')


def sacar_dinheiro():
    global saldo, extrato
    valor_saque = float(input('Quanto você deseja sacar: '))
    if valor_saque > saldo:
        print('Saldo insuficiente!')
    else:
        saldo -= valor_saque
        extrato.append(f'Saque: -R$ {valor_saque:.2f}')
        print(f'Pronto! \nAgora você tem R$ {saldo:.2f} na conta!')
    
    input('Aperte qualquer tecla para continuar!')


def adicionar_compra():
    global saldo, extrato, compras
    print('-----------------------')
    print('1- Essencial')
    print('2- Pessoal')
    print('3- Lazer')
    print('4- Saúde')
    print('-----------------------')
    opcao_compra = input('Qual tipo de compra você deseja adicionar: ')

    tipos = {
        '1': 'essencial',
        '2': 'pessoal',
        '3': 'lazer',
        '4': 'saude'
    }

    if opcao_compra in tipos:
        valor = float(input('Quanto foi gasto: '))
        if valor > saldo:
            print('Saldo insuficiente para esta compra!')
        else:
            tipo = tipos[opcao_compra]
            saldo -= valor
            compras[tipo].append(valor)
            extrato.append(f'Compra ({tipo}): -R$ {valor:.2f}')
            print(f'Compra registrada! Seu novo saldo é R$ {saldo:.2f}')
    else:
        print('Opção inválida!')
    
    input('Aperte qualquer tecla para continuar!')


def acessar_extrato():
    global extrato
    print('--- EXTRATO ---')
    if len(extrato) == 0:
        print('Nenhuma transação registrada.')
    else:
        for transacao in extrato:
            print(transacao)
    print('----------------')
    input('Aperte qualquer tecla para continuar!')


# Loop principal
while True:
    limpar_tela()
    exibir_menu()
    opcao = input('Escolha uma opção: ')
    print('-----------------------')
    
    if opcao == '1':
        acessar_saldo()
    elif opcao == '2':
        adicionar_dinheiro()
    elif opcao == '3':
        sacar_dinheiro()
    elif opcao == '4':
        adicionar_compra()
    elif opcao == '5':
        acessar_extrato()
    elif opcao == '6':
        print('Saindo...')
        break
    else:
        print('Opção inválida!')
        input('Aperte qualquer tecla para continuar!')