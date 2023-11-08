n = int(input('Escolha um número de 0 a 9999: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('O número {} tem:\n'.format(n))
print('Unidade: {};'.format(u))
print('Dezena: {};'.format(d))
print('Centena: {};'.format(c))
print('Milhar: {}.'.format(m))
