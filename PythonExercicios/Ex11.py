largura = int(input('Digite a largura de uma parede em metros: '))
altura = int(input('Digite a altura: '))
area = altura*largura
print('A área da parede é {} m².\nVão ser necessários {} litros de tinta para pintá-la!'.format(area, area*2))