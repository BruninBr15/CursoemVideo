dia = int(input('Por quantos dias o carro foi alugado?\n'))
km = float(input('Quantos kilômetros foram percorrridos?\n'))
aluguel = (dia*60)+(km*0.15)
print('O valor do aluguel do carro ficou em {}R$.'.format(aluguel))