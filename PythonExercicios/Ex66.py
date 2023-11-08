soma = cont = 0

while True:
    n = int(input('Digite um valor (999 pra parar): '))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'Soma dos {cont} valores digitados é {soma}.')
