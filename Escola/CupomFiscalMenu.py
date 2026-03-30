import os 
import sys
from datetime import datetime

#dicionário para armazenar produtos
produtos = {}

#limpar tela
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def continue_prompt():
    input('\nPressione ENTER para continuar...')


def exibir_menu():
    clear_screen()
    print("="*60)
    print(" " * 15 + 'MENU PRINCIPAL')
    print("="*60)
    print(" " * 6+ '1. Adicionar Produto')
    print(" " * 6+ '2. Exibir Produto')
    print(" " * 6+ '3. Gerar Cupom')
    print(" " * 6+ '4. Sair')
    print("="*60)

def adicionar_produto(produto):
    clear_screen()
    produto = input('Digite o nome do produto: ')
    preco = float(input(f'Digite o preço de {produto}: '))
    quantidade = int(input(f'Digite a quantidade de {produto}: '))
    produtos[produto] = {'preco': preco, 'quantidade': quantidade}
    print(f'\nProduto {produto} adicionado com sucesso!')    
    continue_prompt()

def exibir_produtos(produtos):
    clear_screen()
    if not produtos:
        print('Nenhum produto cadastrado.')
    else:
        print(f"{'Produto'}:<20{'Preço':<15}{'Quantidade'}:<12")
        print("="*60)
        for produto, dados in produtos.items():
            print(f"{produtos:<20}{dados['preco']:<15.2f}{dados['quantidade':<12]}")
    continue_prompt()
