from random import randint
from time import sleep

jogos = list()
teste = []

print('-='*15)
print(f'{"MEGA SENA":15^}')
print('-='*15)

quant = int(input('Quantos jogos você quer sortear?\n'))

for x in range(0, quant):

    for i in range(0, 6):
        num = randint(1, 60)
        teste.append(num)

    jogos.append(teste[:])
    teste.clear()

print(f'\tSORTEANDO {quant} JOGOS')

sleep(0.5)

for i in range(0, quant):

    print(f'Jogo {i+1}: {jogos[i]}')

    sleep(0.5)
