distancia = float(input('Qual a distância em Km da sua viagem?\n'))
preco = 0
if distancia <= 200:
    preco = distancia * 0.5
    print('O valor da passagem da sua viagem é R${:.2f}!'.format(preco))
else:
    preco = distancia * 0.45
    print('O valor da passagem da sua viagem é R${:.2f}!'.format(preco))
