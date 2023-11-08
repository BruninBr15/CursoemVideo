from random import randint
from time import sleep
escolha = ('Pedra', 'Papel', 'Tesoura')
bot = randint(0,2)
print('''As opções são: 
0 - PEDRA
1 - PAPEL
2 - TESOURA''')
player = int(input('Qual a sua jogada?\n'))
print('JO...')
sleep(0.5)
print('KEN...')
sleep(0.5)
print('PO!!!')
sleep(0.5)
print('-='*15)
print('O computador escolheu {}!'.format(escolha[bot]))
print('O jogador escolheu {}!'.format(escolha[player]))
print('-='*15)
if bot == 0:
    if player == 0:
        print('EMPATE!')
    elif player == 1:
        print('VITÓRIA DO JOGADOR!')
    elif player == 2:
        print('VITÓRIA DO COMPUTADOR!')
    else:
        print('JOGADA INVÁLIDA!')
elif bot == 1:
    if player == 0:
        print('VITÓRIA DA MÁQUINA')
    elif player == 1:
        print('EMPATE!')
    elif player == 2:
        print('VITÓRIA DO JOGADOR!')
    else:
        print('JOGADA INVÁLIDA!')
elif bot == 2:
    if player == 0:
        print('VITÓRIA DO JOGADOR!')
    elif player == 1:
        print('VITÓRIA DO COMPUTADOR!')
    elif player == 2:
        print('EMPATE!')
    else:
        print('JOGADA INVÁLIDA!')
