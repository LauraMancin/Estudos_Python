#import os

#def limpar_tela():
 # windows cls // linux/mac (clear)
#   os.system('cls' if os.name == 'nt' else 'clear')

lista_compras = []
opcao = 0 

while opcao != 4:
    #limpar_tela()
    print('===== LISTA =====')
    print('1- Adicionar item')
    print('2- Remover item')
    print('3- Ver lista')
    print('4- Sair')
    print('=================')

    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        item = input('Insira o item que deseja adicionar: ')
        lista_compras.append(item)
        print('Item Adicionado!')

    elif opcao == '2':
        if lista_compras == 0:
            print('Não há nada na sua lista')
        else:
            for index, item in enumerate(lista_compras):
                print(index, item)
            index = int(input('Digite o item que deseja remover: '))
            lista_compras.pop(index)
            print('Item Removido!')

    

    elif opcao == '4':
        print('Saindo')