brasileiro = ('Botafogo', 'Palmeiras', 'Bragantino', 'Grêmio', 'Atlético-MG',
              'Flamengo', 'Athletico-PR', 'Fluminense', 'Fortaleza', 'São Paulo',
              'Internacional', 'Cuiabá', 'Corinthians', 'Santos', 'Bahia',
              'Vasco', 'Cruzeiro', 'Goiás', 'Coritiba', 'América-MG')

print(f'Times da Séie A do Campeonato Brasileiro:\n{brasileiro}')

print('-='*20)
print(f'Os 5 no topo da tabela são:\n{brasileiro[:5]}')

print('-='*20)
print(f'Os 4 no rebaixamento são:\n{brasileiro[16:]}')

print('-='*20)
vasco = brasileiro.index('Vasco') + 1
print(f'O Vasco está na {vasco}º posição.')
