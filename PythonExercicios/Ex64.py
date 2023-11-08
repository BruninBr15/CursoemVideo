from time import sleep

n = cont = soma = 0

while n != 999:

    n = int(input('Digite um número (999 para parar): '))

    if n != 999:

        cont += 1
        soma += n

print('\nParando o programa...\n')
sleep(0.5)

print('Foram digitados {} números, e a soma deles é {}.'.format(cont, soma))
