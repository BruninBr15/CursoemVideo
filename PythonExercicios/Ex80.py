from time import sleep

num = []

for i in range(0, 5):

    n = int(input('Digite um número: '))

    '''if i == 0:
        num.append(n)  #É o primeiro item a ser incluído, então vai pro final.
    elif n > num[-1]:
        num.append(n)  #Se for maior que o atual último número da lista, ele vai pro final à direita desse número.'''

    if i == 0 or n > num[-1]:
        num.append(n)
        print(f'O {n} foi para o final da lista;')

    else:

        cont = 0
        while cont < len(num):  #Analisa cada valor da lista, se for menor ou igual, empurra e ocupa o espaço.
            if n <= num[cont]:
                num.insert(cont, n)
                print(f'O {n} foi para a posição {cont} da lista;')
                break

            cont += 1

sleep(1)

print('-='*21)

print('A lista ordenada dos números é: ', end='')
for i in num:
    print(f'{i}', end=' ')
