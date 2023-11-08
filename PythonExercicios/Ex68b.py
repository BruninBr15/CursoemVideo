from random import randint

win = 0

while True:

    bot = randint(0, 6)
    player = int(input('Jogue um número: '))
    escolha = str(input('Qual o seu chute (P/I): ')).strip().upper()[0]
    print('-=' * 15)

    if (bot + player) % 2 == 0:
        res = 'PAR'
    else:
        res = 'ÍMPAR'

    print(f'O computador jogou {bot} e você {player}. O total deu {bot + player} que é {res}!')
    print('-=' * 15)

    if escolha == 'P':
        if res == 'PAR':
            win += 1
            print('Vitória do Jogador! Parabéns!!!')
        else:
            print('Derrota! Tente na próxima!')
            break

    else:
        if res == 'ÍMPAR':
            win += 1
            print('Vitória do Jogador! Parabéns!!!')
        else:
            print('Derrota! Tente na próxima!')
            break

print('<>' * 15)
print(f'Você venceu {win} vezes. Tente de novo!')
