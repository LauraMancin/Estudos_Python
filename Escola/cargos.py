cargo = input('Insira o seu cargo: ').strip().lower()
dia = input('Digite o dia da semana: ').strip().lower()

if cargo==('gerente'):
if dia==('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado'):
    print('Acesso Válido!')
elif cargo==('analista') and dia==('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta'):
    print('Acesso Válido!')
elif cargo==('estagiário') and dia==('Segunda', 'Quarta', 'Sexta'):
    print('Acesso Válido!')
else:
    print('Acesso Inválido')
