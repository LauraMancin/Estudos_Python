#Cateto e Hipotenusa
import math
cateto1=int(input('Digite o Primeiro Cateto: '))
cateto2=int(input('Digite o Segundo Cateto: '))
hipotenusa= math.sqrt(cateto1**2 + cateto2**2)
print('O valor da Hipotenusa de {} + {} é {}'.format(cateto1,cateto2,hipotenusa))
