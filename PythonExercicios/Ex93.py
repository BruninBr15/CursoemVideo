jogador = dict()
gols_partidas = list()
total_gols = 0

jogador['nome'] = str(input('Nome do jogador: ')).strip()

jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

for cont in range(0, jogador['partidas']):
    gols_partidas.append(int(input(f'\tQuantos gols na partida {cont+1}? ')))
jogador['gols'] = gols_partidas.copy()

jogador['total'] = sum(gols_partidas)

print('-='*15)
print(jogador)
print('-='*15)

for k, v in jogador.items():
    print(f'{k} é {v}')

print('-='*15)

#  print(f'O jogador {jogador["nome"]} jogou {jogador["partidas"]} partidas.')
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')

for i, v in enumerate(gols_partidas):
    print(f' - Na partida {i+1}, fez {v} gols')
    total_gols += v
print(f'Fez um total de {total_gols} gols!')
