cont = 0
n = int(input('Digite um número: '))
for x in range(1, n+1):
    if n % x == 0:
        print('\033[32m', end=' ')
        cont = cont + 1
    else:
        print('\033[31m', end=' ')
    print(x, end=' ')
print('\n\033[m', '-='*15)
print('O número {} foi dividido {} vezes.'.format(n, cont))
if cont == 2:
    print('{} É um número primo.'.format(n))
else:
    print('{} NÃO é um número primo.'.format(n))
