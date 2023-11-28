'''brasil = list()
estado1 = {'UF': 'Minas Gerais', 'sigla': 'MG'}
estado2 = {'UF': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[0]['UF'])'''
estado = dict()
brasil = list()
for cont in range(0, 3):
    estado['UF'] = str(input('Estado: ')).strip()
    estado['sigla'] = str(input('Sigla: ')).strip()
    brasil.append(estado.copy())
for est in brasil:
    for v in est.values():
        print(f'{v}', end=' ')
    print()
