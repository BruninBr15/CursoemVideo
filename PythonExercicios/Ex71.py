print('-='*15)
print('\t\tBANCO PYTHON')
print('-='*15)

valor = int(input('Informe o valor a ser sacado: R$'))
total = valor

ced = 50
quant_ced = 0

while True:

    if total >= ced:
        total -= ced
        quant_ced += 1

    else:

        if quant_ced > 0:
            print(f'{quant_ced} de R${ced}!')

        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1

        quant_ced = 0

        if total == 0:
            break
print('\nSaque terminado!! Volte sempre!')
