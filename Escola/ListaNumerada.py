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
    for i,item in enumerate(lista_compras, start=1):
        print(f' {i} - {item}')