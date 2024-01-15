from time import sleep

pessoa = dict()
ficha = list()

soma_idade = 0

while True:

    pessoa.clear()

    pessoa['nome'] = str(input('Nome: ')).strip()

    while True:
        pessoa['sexo'] = str(input('Sexo (M/F): ')).strip().upper()[0]
        if pessoa['sexo'] not in 'MF':
            print('SEXO INVÁLIDO!!  Digite apenas M ou F.')

        else:
            break

    pessoa['idade'] = int(input('Idade: '))

    soma_idade += pessoa['idade']

    ficha.append(pessoa.copy())

    while True:
        resp = str(input('Deseja continuar (S/N)?\n')).strip().upper()[0]
        if resp not in 'SN':
            print('RESPOSTA INVÁLIDA!! Apenas S ou N.')
        else:
            break

    if resp == 'N':
        break

print('<>'*17)
sleep(1)

print(f'Ao todo {len(ficha)} pessoas foram cadastradas!')

media = soma_idade / len(ficha)
print(f'A média de idade do grupo é {media:.2f} anos!')

print('As mulheres cadastradas são: ', end='')
for i in ficha:
    if i['sexo'] == 'F':
        print(i['nome'], end=' ')

print()
print('As pessoas com uma idade acima da média são: ', end='')
for i in ficha:
    if i['idade'] > media:
        print(i['nome'], end=' ')
