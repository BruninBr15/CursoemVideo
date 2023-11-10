num = []
pares = list()
impares = []

cont = 0

while True:

    num.append(int(input('Digite um número: ')))

    resp = str(input('Quer continuar (S/N)?\n')).strip().upper()[0]
    if resp == 'N':
        break

for x in num:
    if x % 2 == 0:
        pares.append(x)
    else:
        impares.append(x)

print('<>'*20)

print(f'Os números digitados são: {num}')

print(f'Os valores pares são {pares}')

print(f'E os ímpares {impares}')
