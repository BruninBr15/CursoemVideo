sexo = str(input('Informe o seu sexo (M/F): ')).strip().upper()[0]#se digitar masculino e feminino, pega só a
# primeira letra
while sexo not in 'MF':
    sexo = str(input('Sexo inválido! Por favor, informe o seu sexo (M/F): ')).strip().upper()
print('Sexo {} registrado com sucesso!'.format(sexo))
