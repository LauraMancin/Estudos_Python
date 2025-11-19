# menu 4 opções, cadastro nome e idade, remover cadastro, ver participantes, sair
import os 

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

cadastro = []

def novo_cadastro():
    novo = input('Você é novo? (S/N): ').lower()

    if 's' in novo:
        nome = input('Qual seu nome: ')
        idade = int(input('Qual sua idade: '))

        pessoa = {'nome': nome, 'idade': idade}
        cadastro.append(pessoa)
        print('Cadastro realizado com sucesso!')
        input("Pressione Enter para continuar...")


    else:
        print('Você já está cadastrado!')
        input("Pressione Enter para continuar...")



def remover_cadastro():
    if len(cadastro) == 0:
        print('Nenhum cadastro realizado!')
        return 
    input("Pressione Enter para continuar...")

    
    remover = input('Digite o nome que deseja remover: ')
    for pessoa in cadastro:
        if pessoa['nome'] == remover:
            cadastro.remove(pessoa)
            print(f'{remover} foi removida com sucesso!')
            return
        input("Pressione Enter para continuar...")
    
    print('Cadastro não encontrado!')
    input("Pressione Enter para continuar...")

def listar_participantes():
    if len(cadastro) == 0:
        print('Nenhum cadastro a ser listado!')
    else:
        print('\n=== LISTA DE CADASTROS ===')
        for pessoa in cadastro:
            print(f"{pessoa['nome']} - {pessoa['idade']} anos")

    input("Pressione Enter para continuar...")


def menu():
    while True:
        limpar_tela()
        print('\nMENU')
        print('1- Cadastrar pessoa')
        print('2- Remover pessoa')
        print('3- Lista de cadastros')
        print('4- Sair')

        escolha = input('Escolha uma opção: ')

        if escolha == '1':
            novo_cadastro()
        elif escolha == '2':
            remover_cadastro()
        elif escolha == '3':
            listar_participantes()
        elif escolha == '4':
            print('Saindo... Até mais!!')
            break
        else:
            print('Escolha inválida.')

menu()