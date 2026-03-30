#Salário Antigo com 15% de aumento
salario = float(input('Qual seu salário atual: '))
a = salario + (salario * 15 / 100)
print(' Seu antigo salario era{:.2f}, e agora seu novo salário, com aumento de 15% é {:.2f}'.format(salario,a))