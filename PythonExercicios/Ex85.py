valores = [[], []]

for i in range(0, 7):

    valor = (int(input(f'Digite o {i+1}º valor: ')))

    if valor % 2 == 0:
        valores[0].append(valor)
    else:
        valores[1].append(valor)

valores[0].sort()
valores[1].sort()

print('<>'*23)

print(f'Os números pares digitados são {valores[0]}')
print(f'Os valores ímpares são {valores[1]}')
