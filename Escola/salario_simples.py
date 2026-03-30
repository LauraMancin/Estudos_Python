#calcular horas trabalhadas por dia

#Tela de entrada
print('='*40)
print(f'{'SISTEMA DE CONTROLE DE HORAS':^40}')
print('='*40)

#Entrada de Dados
nome = input('Digite seu nome: ').capitalize()
numfun = int(input('Digite seu número de identificação: '))
salario = float(input('Digite seu salário por hora (R$): '))
hora = int(input('Digite quantas horas trabalhou hoje: '))

#Calculo do salario
salario_total = salario * hora

#Tela de saida
print('\n' + '='*40)
print(f'{'FOLHA DE PAGAMENTO DIÁRIA':^40}')
print('='*40)
print(f'{'Nome':20}: {nome}')
print(f'{'Identificação':<20}: {numfun}')
print(f'{'Horas Trabalhadas':<20}: {hora}')
print(f'{'Salário por Hora':<20}:{salario:.2f}')
print(f'{'Salário do Dia':<20}: {salario_total}')
print('='*40)