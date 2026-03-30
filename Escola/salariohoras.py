#Pedindo informações do funcionário

nome = input('Digite o seu nome: ')
numero = float(input('Qual o número do funcionário: '))
salario = int(input('Digite o salário por horas: '))
horas = float(input('Quantas horas foram trabalhadas hoje: '))

#calcula o salário 
salario_total = salario * horas

#mostra o resultado
print(f'| Nome: {nome}')
print(f'| Identificação {numero}')
print(f'| Horas trabalhadas: {horas}')
print(f'| Salário-Horas: {salario_total:.2}')