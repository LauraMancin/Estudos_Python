#criando variavel 
lista_compras = []

while True: 
    produto = input('Digite o nome de um produto (ou "sair" para encerrar): ')

#verificando se o usuário quer sair

    if produto.lower() == "sair":
        break

#adicionando o produto na lista
    lista_compras.append(produto)

#mostrar lista atualizad
    print('\n lista de compras: ')
    for item in lista_compras:
        print(f' - {item}')