from random import randint
bot = randint(0, 10)
tentativas = 0
print('Vamos jogar um jogo!\nAcabei de pensar em um número entre 0 a 10, tente adivinhar.')
print('-='*35)
player = ''
while player != bot:
    player = int(input('Qual o seu palpite?\n'))
    tentativas += 1
    if player != bot:
        if bot > player:
            print('Errou, que pena! Tente um número maior!')
        else:
            print('Errou, que pena! Tente um número menor!')
print('\nParabéns!!\nVocê venceu em {} tentaivas!'.format(tentativas))
