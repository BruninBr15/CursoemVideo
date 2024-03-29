from random import randint
from time import sleep
from operator import itemgetter

jogo = {
    'player1': randint(1, 20),
    'player2': randint(1, 20),
    'player3': randint(1, 20),
    'player4': randint(1, 20)
}

ranking = dict()

print('SORTEIO: ')

for k, v in jogo.items():
    print(f'O {k} tirou {v} no dado!')
    sleep(0.7)

print("-="*15)
print('RANKING')
print("-="*15)
sleep(1)

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)  # 0 ele coloca em ordem de chave, em 1 de valor

for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')
