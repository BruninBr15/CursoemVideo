from random import randint

numeros = (randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9))

print('Os valores escolhidos foram: ', end='')
for x in numeros:
    print(f'{x}', end=' ')

print(f'\nO maior valor foi {max(numeros)} e o menor foi {min(numeros)}.')
