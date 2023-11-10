num = []

maior = menor = 0

for x in range(0, 5):

    num.append(int(input('Digite um número: ')))

    if x == 0:
        maior = menor = num[x]

    else:
        if x > maior:
            maior = num[x]

        elif x < menor:
            menor = num[x]

print('<>'*16)

print(f'O MENOR valor é {menor} nas posições:', end=' ')
for i, x in enumerate(num):

    if x == menor:
        print(f'{i+1}', end=' ')

print(f'\nO MAIOR valor é {maior} nas posições:', end=' ')
for i, x in enumerate(num):

    if x == maior:
        print(f'{i+1}', end=' ')
