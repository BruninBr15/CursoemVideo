'''
co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
a = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa é {}.'.format(a))
'''

from math import hypot
co = float(input('Informe o cateto oposto do triângulo: '))
ca = float(input('Informe o cateto adjacente: '))
a = hypot(co, ca)
print('A hipotenusa do triângulo retângulo é {:.2f}.'.format(a))
