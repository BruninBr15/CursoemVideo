inicio = int(input('Digite o inicio: '))
fim = int(input('Digite o fim: '))
passo = int(input('Digite o passo: '))
soma = 0
for x in range(inicio, fim, passo):
    print(x)
    soma = soma + x
print('FIM! A soma deu {}.'.format(soma))