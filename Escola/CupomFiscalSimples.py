#script para criar um cupom fiscal simples

from datetime import datetime

#dicionário
produtos = {}

#inserindo dados

while True:
    produto = input('Digite o nome do produto (ou "sair" para finalizar): ')
    if produto.lower() == 'sair':
        break
    preco = float(input(f'Digite o preço de {produto}: '))
    quantidade = int(input(f'Digite a quantidade de {produto}: '))
    produtos[produto] = {'preco': preco, 'quantidade': quantidade}

#pegando a data e hora atual
data_hora = datetime.now().strftime("%d%m%Y %H:%M:%S")

#cabeçalho
print("\n" + "="*60)
print(" "*20 + 'CUMPOM FISCAL SIMPLES')
print("="*60)
print('Data e Hora: ', data_hora)
print("="*60)
print(f'{'Produto':<20}{'Preço':<15}{'Quantidade':<12}{'SubTotal':<10}')
print("="*60)

#listando os produtos e calculando o total
total_geral = 0
for produto, dados in produtos.items():
    subtotal = dados['preco'] * dados['quantidade']
    total_geral += subtotal
    print(f"{produto:<20}{dados['preco']:<15.2f}{dados['quantidade']:<12}{subtotal:<10.2f}")

print("="*60)
print(f"{'TOTAL GERAL: ':<44}{total_geral:>8.2f}")
print("="*60)
print('Obrigada pela preferência!')
