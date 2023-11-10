num = list()

while True:

    num.append(int(input('Digite um valor: ')))

    resp = str(input('Deseja continuar (S/N)?\n')).strip().upper()[0]
    if resp == 'N':
        break

print('<>'*15)

print(f'Foram adicionados {len(num)} números na lista!')

num.sort(reverse=True)
print(f'A lista em ordem decrescente fica {num}')

if 5 in num:
    print(f'O 5 está na lista.')
else:
    print('O 5 não está na lista.')
