soma = 0
cont = 0
for x in range(0,6):
    n = int(input('Digite {} número: '.format(x)))
    if n % 2 == 0:
        soma = soma + n
        cont = cont + 1
print('A soma dos {} números pares digitados é {}!'.format(cont, soma))
