salario = float(input('Informe o seu salário na empresa: '))
if salario <= 1250:
    salario = salario * 1.15
else:
    salario = salario * 1.10
print('Seu novo salário é R${:.2f}!'.format(salario))
