print('='*30)
print(f'{"Materiais Escolares":^30}')
print('='*30)

tabela_precos = ('Lápis', 1.25,
                 'Borracha', 1.00,
                 'Lapiseira', 2.00,
                 'Caderno', 30.00,
                 'Estojo', 15.50,
                 'Caneta', 4.75,
                 'Mochila', 170.50,
                 )

for x in range(0, len(tabela_precos)):

    if x % 2 == 0:
        print(f'{tabela_precos[x]:.<22}', end='')

    else:
        print(f'R${tabela_precos[x]:>5}')

print('='*30)
