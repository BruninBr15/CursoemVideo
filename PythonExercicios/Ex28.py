from time import sleep
from random import randint
n_maquina = randint(0, 5)#O computador vai escolher um número INTEIRO aleatoriamente entre 0 e 5
print('-=-'*25)
print('Tente adivinhar em qual número entre 0 e 5 eu estou pensando...')
print('-=-'*25)
n_jogador = int(input('Qual número eu escolhi??\n'))
print('CARREGANDO...')
sleep(2)
if n_maquina == n_jogador:
    print("Você Acertou!\nParabéns!!")
elif n_jogador > 5 or n_jogador < 0:
    print('NÚMERO INVÁLIDO!')
else:
    print('Você Errou! Eu escolhi o {}.\nQuem sabe na próxima.'.format(n_maquina))
