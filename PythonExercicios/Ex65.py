resp = 'S'
n = cont = soma = maior = menor = media = 0

while resp == 'S':

    n = int(input('Digite um número: '))
    cont += 1
    soma += n

    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor: 
            menor = n

    resp = str(input('Deseja continuar? (S/N)\n')).strip().upper()[0]

print('-'*15)

media = soma/cont
print('A média dos valores lidos é {:.2f}.\nO menor valor é {} e o maior é {}.'.format(media, menor, maior))
