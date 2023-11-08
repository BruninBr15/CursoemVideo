velocidade = float(input('Informe a velocidade atual do seu carro em Km/h: '))
if velocidade > 80:
    print('Você ultrapassou o limite e foi multado!')
    multa = (velocidade - 80) * 7
    print('A multa a ser paga é de R${:.2f}!'.format(multa))
print('Bom dia! Dirija com cuidado.')
