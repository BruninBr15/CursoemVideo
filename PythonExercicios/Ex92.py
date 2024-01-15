from datetime import datetime

pessoa = dict()

pessoa['nome'] = str(input('Nome completo: ')).strip()

ano_nasc = int(input('Ano de nascimento: '))

ano_atual = datetime.now().year
pessoa['idade'] = ano_atual - ano_nasc

pessoa['CTPS'] = int(input('Carteira de Trabalho (0 se não possuir): '))

if pessoa['CTPS'] != 0:
    pessoa['contratação'] = int(input('Ano da contratação: '))

    pessoa['salário'] = float(input('Salário atual: R$'))

    pessoa['aposentadoria'] = pessoa['idade'] + ((pessoa['contratação'] + 35) - ano_atual)

print('<>'*18)

for k, v in pessoa.items():
    print(f'{k} é: {v}')
