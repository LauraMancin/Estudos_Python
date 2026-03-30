#Quanto a pessoa tem na carteira e quantos dólares ela pode comprar (Considerando: U$1.00 = R$3.27)
real=float(input('Quantos reais você tem na carteira? R$'))
dolar=real/3.27
print('Considerando que o dolar está U$3.27 você pode comprar com R$ {}, U$ {:.2f}'.format(real,dolar))
