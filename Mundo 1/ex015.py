#Aluguel de Veículo
tempo=float(input('Informe quantos dias você usou este veículo: '))
km=float(input('Informe quantos km foram rodade: '))
pago=(tempo * 60) + (km * 0.15)
print('Baseado em {} dias e em {} km rodados, o total a pagar é {}'.format(tempo,km,pago))
