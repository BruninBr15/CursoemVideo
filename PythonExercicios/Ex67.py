while True:
    n = int(input('Digite um númeor para mostar a tabuada (negativo pra parar): '))

    print('-=' * 20)

    if n < 0:
        break
    for x in range(0,11):
        print(f'{n} X {x} = {n*x}')

    print('-='*20)

print('FIM! Programa encerrado, volte sempre.')
