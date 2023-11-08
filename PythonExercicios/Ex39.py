from datetime import date
nasc = int(input('Informe o ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - nasc
print('Você tem {} anos em {}.'.format(idade, ano_atual))
if idade < 18:
    print('Não está na hora de se alistar!\nEle será em {}.'.format(ano_atual + (18 - idade)))
elif idade == 18:
    print('Já está na hora de fazer seu alistamento!')
else:
    print('Já passou a data do seu alistamento.\nEle ocorreu em {}.'.format(ano_atual - (idade-18)))
