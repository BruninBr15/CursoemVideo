n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite outro número: '))
n4 = int(input('Digite o último número: '))

numeros = n1, n2, n3, n4

print('-='*15)
print(f'Os números digitados são: {numeros}')

print(f'O 9 apareceu {numeros.count(9)} vezes.')

if 3 in numeros:
    print(f'O 3 apareceu na {numeros.index(3)+1}º posição.')

print('Os números pares são: ', end='')
for x in numeros:
    if x % 2 == 0:
        print(f'{x}', end=' ')
