opcoes = 0
while opcoes!=5:


print(*40)
print(f'{'CALCULADORA':.^40}')
print(*40)
opcoes = int(input('''Digite suas opções:
[1] - Somar dois número
[2] - Subtrair dois números
[3] - Multiplicar dois números
[4] - Dividir dois números
[5] - Sair do programa
'''))

print(*40)

if opcoes==1:
numero1= float(input('Digite um número: '))
numero2= float(input('Digite um número: '))
soma = numero1 + numero2
print(f'Soma entre os dois números apresentados: {soma} ')
elif opcoes ==2:
numero1= float(input('Digite um número: '))
numero2= float(input('Digite um número: &#39;'))
subtrair = numero1 - numero2
print(f'a subtração entre os dois números apresentados é: {subtrair}')
elif opcoes ==3:
numero1= float(input('Digite um número: ';))
numero2= float(input('Digite um número: '))
multiplicar = numero1 * numero2
print('A multiplicação entre os dois númerosa apresentados é: {multiplicar}';)
elif opcoes ==4:
numero1= float(input('Digite o primeiro número: '))
numero2= float(input('Digite o segundo número: '))
if numero1==0 or numero2==0:
print('Digite um número diferente de 0!')
else:
divisão = numero1/numero2
elif opcoes==5:
print('Saindo!')
break
else:

print('Número inválido, tente novamente!')