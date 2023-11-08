from time import sleep
valor1 = float(input('Primeiro valor: '))
valor2 = float(input('Segundo valor: '))
opcao = 0

while opcao != 5:

    print('''    1 - Soma
    2 - Multiplicação
    3 - Maior e Menor
    4 - Troca de Números
    5 - Sair do Programa''')
    opcao = int(input('Qual opção você quer?\n'))

    if opcao == 1:
        print('{} + {} = {}'.format(valor1, valor2, valor1+valor2))

    elif opcao == 2:
        print('{} X {} = {}'.format(valor1, valor2, valor1*valor2))

    elif opcao == 3:
        if valor1 > valor2:
            print('O menor é {} e o maior é {}.'.format(valor2, valor1))
        else:
            print('O menor é {} e o maior é {}.'.format(valor1, valor2))

    elif opcao == 4:
        print('Digite os valores novamente.')
        valor1 = float(input('Primeiro valor: '))
        valor2 = float(input('Segundo valor: '))

    elif opcao == 5:
        print('Finalizando...')
        sleep(1)

    else:
        print('OPÇÃO INVÁLIDA! Tente de novo.')
        break

    print('-='*20)

print('Fim do programa! Aguardamos você aqui de novo.')
