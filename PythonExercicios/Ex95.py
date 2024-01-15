jogador = dict()
time = list()
gols_partidas = list()

while True:
    jogador.clear()

    jogador['nome'] = str(input('Nome do jogador: ')).strip()

    jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

    for cont in range(0, jogador['partidas']):
        gols_partidas.append(int(input(f'\tQuantos gols na partida {cont+1}? ')))

    jogador['gols'] = gols_partidas.copy()

    jogador['total'] = sum(gols_partidas)

    time.append(jogador.copy())

    gols_partidas.clear()

    while True:
        resp = str(input('Deseja continuar (S/N)? ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO!! Resposta Inválida, somente S ou N!')
    if resp == 'N':
        break

print('-='*21)

print('Cód.', end='  ')
for k in jogador.keys():
    print(f'{k:<15}', end=' ')

print()

for cod, d in enumerate(time):
    print(f'{cod:<5}', end=' ')
    for v in d.values():
        print(f'{str(v):<15}', end=' ')
    print()

print('-='*21)

while True:
    busca = int(input('Deseja analisar qual jogador (999 para terminar): '))
    if busca == 999:
        break
    if busca >= len(time):
        print('Código inexistente!! Tente novamente!')

    else:
        print(f'\n\tANÁLISE DO JOGADOR {time[busca]["nome"]}\t')
        for i, g in enumerate(time[busca]["gols"]):
            print(f'\tNa partida {i+1} fez {g}!')

    print('<>'*21)

print('\nPrograma Encerrado!! Volte sempre!')
