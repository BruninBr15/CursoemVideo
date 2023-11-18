matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

pares = soma3coluna = maior = 0

for linha in range(0, 3):

    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))

        if linha == 1 and coluna == 0:
            maior = matriz[linha][coluna]

print('~~' * 20)

for linha in range(0, 3):

    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^4}]', end=' ')

        if matriz[linha][coluna] % 2 == 0:
            pares += matriz[linha][coluna]

        if matriz[1][coluna] > maior:
            maior = matriz[1][coluna]

    print()

    soma3coluna += matriz[linha][2]

print(f'A soma de todos os valores pares é {pares}!')

print(f'A soma dos valores da terceira coluna é {soma3coluna}!')

print(f'O maior número da segunda linha é {maior}!')
