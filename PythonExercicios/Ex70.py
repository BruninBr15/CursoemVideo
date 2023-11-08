res = cheap_str = ''
total = thousand = cheap = cont= 0

print('-='*15)
print('MERCADÃO')
print('-=' * 15)

while True:

    prod = str(input('Produto comprado: '))

    cont += 1

    price = float(input('Preço do produto: R$'))

    if cont == 1:
        cheap_str += prod
        cheap += price
    else:
        if price < cheap:
            cheap_str = prod
            cheap = price

    total += price
    if price > 1000:
        thousand += 1

    res = str(input('Deseja continuar?\n')).strip().upper()[0]
    if res == 'N':
        break

print('<>'*15)
print('\tPAGAMENTO')
print(f'A compra dos {cont} produtos vai custar R${total:.2f}.')
print(f'{thousand} produtos custaram mais de R$1000.00!')
print(f'O mais barato foi {cheap_str} que custou R${cheap:.2f}!')
