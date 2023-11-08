maior_peso = 0
menor_peso = 0
total = 0
pesos = []
for x in range(0, 5):
    pesos.append(float(input('Digite o peso da {}º pessoa: '.format(x+1))))
    if x == 0:
        menor_peso = pesos[x]
        maior_peso = pesos[x]
    else:
        if pesos[x] < menor_peso:
            menor_peso = pesos[x]
        elif pesos[x] > maior_peso:
            maior_peso = pesos[x]
    total = total + pesos[x]
media = total / 5
print('-='*15)
print('A média de peso dessas 5 pessoa é {:.2f}.'.format(media))
print('A pessoa de menor peso tem {}kg e a de maior peso tem {}kg!'.format(menor_peso, maior_peso))
