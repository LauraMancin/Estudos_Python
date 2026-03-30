#setar variavel
opcao = ''

while opcao != '4':
    print('-'*20)
    print('   MENU DE OPÇÕES')
    print('-'*20)
    print('1- Dizer Olá')
    print('2- Somar dois números')
    print('3- Subtrair dois números')
    print('4- Sair')
    print('-'*20)

    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        print('Olá! Tudo bem? ')
    elif opcao == '2':
        num1 = float(input('Digite o primeiro número: '))
        num2 = float(input('Digite o segundo número: '))
        soma = num1 + num2
        print(f'A soma de {num1} e {num2} é {soma}')
    elif opcao == '3':
        num1 = float(input('Digite o primeiro número: '))
        num2 = float(input('Digite o segundo número: '))
        subtracao = num1 - num2
        print(f'A subtração de {num1} e {num2} é {subtracao}')
    elif opcao == '4':
        print('Saindo do Programa, até mais!')
    else:
        print('Opção inválida. Escolha uma das opções do Menu')