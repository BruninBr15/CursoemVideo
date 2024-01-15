aluno = dict()

aluno['Nome'] = str(input('Nome do aluno: ')).strip()

aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))

if 7 <= aluno['Média'] <= 10:
    aluno['Situação'] = 'Aprovado'

elif 4 <= aluno['Média'] < 7:
    aluno['Situação'] = 'Exame'

else:
    aluno['Situação'] = 'Reprovado'

print('<>'*10)

for k, v in aluno.items():
    print(f'\t{k} é {v}')

