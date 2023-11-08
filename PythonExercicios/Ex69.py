older = men = ladys = 0

while True:
    print('-' * 25)
    print('Cadatro')
    print('-'*25)

    idade = int(input('Digite a idade: '))
    if idade > 18:
        older += 1

    sexo = str(input('Informe o sexo (M/F): ')).strip().upper()[0]
    if sexo == 'M':
        men += 1
    elif sexo == 'F' and idade < 20:
        ladys += 1
    else:
        print('SEXO INVÁLIDO!')
        break

    res = str(input('Quer continuar ?\n')).strip().upper()[0]
    if res == 'N':
        break

print('<>'*15)
print(f'O total de pessoas com mais de 18 anos são {older}.')
print(f'{men} homens foram cadastrados.')
print(f'São {ladys} mulheres com menos de 20 anos.')
