dados = list()
pessoa = list()


while True:

    pessoa.append(str(input('Nome: ')))
    pessoa.append(float(input('Peso: ')))
    dados.append(pessoa[:])
    pessoa.clear()

    resp = str(input('Deseja prosseguir (S/N)?\n')).strip().upper()[0]
    if resp == 'N':
        break

print('-='*21)

print(f'Foram cadastradas {len(dados)} pessoas!')

maior = menor = dados[0][1]
for i in dados:

    if i[1] > maior:
        maior = i[1]
    elif i[1] < menor:
        menor = i[1]

print(f'O maior peso é {maior}Kg. As pessoas com esse peso são ', end='')
for i in dados:
    if i[1] == maior:
        print(f'{i[0]}', end=' /')

print(f'\nJá o menor é {menor}Kg. As pessoas com esse peso são ', end='')
for i in dados:
    if i[1] == menor:
        print(f'{i[0]}', end=' /')
