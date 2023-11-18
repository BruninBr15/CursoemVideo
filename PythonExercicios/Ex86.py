matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for linha in range(0, 3):

    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um número para [{linha}, {coluna}]: '))

print('_=' * 20)

for linha in range(0, 3):

    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^4}]', end=' ')

    print()
