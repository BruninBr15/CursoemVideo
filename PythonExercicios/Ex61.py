print('-='*15)
print('10 TERMOS DE UMA P.A.')
print('-='*15)

primeiro = int(input('Digite o primeiro termo da P.A.: '))
razao = int(input('Digite a razão dela: '))
cont = 0

while cont < 10:

    print('{} - '.format(primeiro), end='')
    primeiro += razao

    cont += 1

print('FIM')