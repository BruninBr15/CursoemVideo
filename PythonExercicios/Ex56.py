total_idade = 0
idade_velho = 0
nome_velho = ''
quant_f = 0
for x in range(0, 4):
    print('------{}º Pessoa------'.format(x+1))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    total_idade = total_idade + idade
    sexo = str(input('Sexo (M/F): ')).strip().upper()
    if x == 0 and sexo == 'M':
        idade_velho = idade
        nome_velho = nome
    if sexo == 'M' and idade > idade_velho:
        idade_velho = idade
        nome_velho = nome
    if sexo == 'F' and idade < 18:
        quant_f = quant_f + 1
media = total_idade / 4
print('\nA média de idade do grupo é {}.'.format(media))
print('O homem mais velho se chama {} e tem {} anos.'.format(nome_velho, idade_velho))
print('{} mulheres do grupo tem menos de 18 anos.'.format(quant_f))