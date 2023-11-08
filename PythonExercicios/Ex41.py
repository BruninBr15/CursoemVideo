from datetime import date
ano_nasc= int(input('Digite o ano do seu nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nasc
print('Você tem {} anos.\n'.format(idade))
if idade <= 9:
    print('A sua categoria é a MIRIM!')
elif idade <= 14:
    print('Sua categoria é a INFANTIL!')
elif idade <= 19:
    print('Sua categoria é a JÚNIOR!')
elif idade <= 25:
    print('Sua categoria é a SÊNIOR!')
else:
    print('Sua categoria é a MASTER!')
