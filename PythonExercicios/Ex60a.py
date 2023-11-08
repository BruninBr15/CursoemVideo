n = int(input('Digite um número: '))
fat = 1
cont = 1

print('Calculando {}! = '.format(n), end='')

while cont <= n:

    fat *= cont

    print('{}'.format(cont), end='')
    if cont < n:
        print(' X ', end='')
    else:
        print(' = ', end='')

    cont += 1

print('{}'.format(fat))
