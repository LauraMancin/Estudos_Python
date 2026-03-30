#criando variavel 
lista_compras = []

while True: 
    produto = input('Digite o nome de um produto, "remover nome_do_produto" para remover ou "sair" para encerrar: ')


#verificando se o usuário quer sair

    if produto.lower() == "sair":
        break

#verificando se o usuário quer remover um produto
    if produto[:8].lower() == "remover ":
        item_remover = produto[8:].strip()
        if item_remover in lista_compras:
            lista_compras.remove(item_remover)
            print(f'O produto "{item_remover}" foi removido da lista')
        else:
            print('O produto "{item_remover}" não está na lista')
        
    else:
        lista_compras.append(produto)
        print(f"{produto} foi adicionado à lista.")