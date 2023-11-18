from random import randint
from time import sleep

jogos = list()
teste = []

print('-='*15)
print(f'{"MEGA SENA":^30}')
print('-='*15)

quant = int(input('Quantos jogos você quer sortear?\n'))

for x in range(0, quant):

    for i in range(0, 6):
        num = randint(1, 60)
        if num not in teste:  #Para não sortear números repetidos
            teste.append(num)
        else:
            num = randint(0, 60)
            teste.append(num)

    teste.sort()
    jogos.append(teste[:])
    teste.clear()

print(f'\t\tSORTEANDO {quant} JOGOS')

sleep(1)

for i in range(0, quant):

    print(f'Jogo {i+1}: {jogos[i]}')

    sleep(1)
