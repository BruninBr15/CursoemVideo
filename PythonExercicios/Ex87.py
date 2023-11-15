matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

pares = soma3j = maior = 0

for i in range(0, 3):

    for j in range(0, 3):
        matriz[i][j] = int(input(f'Digite um valor para [{i}, {j}]: '))

        if i == 1 and j == 0:
            maior = matriz[i][j]

print('~~' * 20)

for i in range(0, 3):

    for j in range(0, 3):
        print(f'[{matriz[i][j]:^4}]', end=' ')

        if matriz[i][j] % 2 == 0:
            pares += matriz[i][j]

        if matriz[1][j] > maior:
            maior = matriz[1][j]

    print()

    soma3j += matriz[i][2]

print(f'A soma de todos os valores pares é {pares}!')

print(f'A soma dos valores da terceira coluna é {soma3j}!')

print(f'O maior número da segunda linha é {maior}!')
