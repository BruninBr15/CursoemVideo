print('-='*15)
print('10 TERMOS DE UMA P.A.')
print('-='*15)

primeiro = int(input('Digite o primeiro termo da P.A.: '))
razao = int(input('Digite a razão dela: '))

cont = 0
termos = 0
mais = 10

while mais != 0:

    termos += mais

    while cont < termos:

        print('{} - '.format(primeiro), end='')
        primeiro += razao

        cont += 1

    print('PAUSA!')
    print('')

    mais = int(input('Quanto mais termos você quer mostrar: '))

print('FIM!')
print('-'*20)
print('Foram mostrados, no total, {} termos da P.A..'.format(termos))