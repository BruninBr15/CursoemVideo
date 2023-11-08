n = soma = 0

while True:
    n = int(input('Digite um número (999 pra parar): '))
    if n == 999:
        break
    soma += n
print(f'A soma dos números é {soma}.')
