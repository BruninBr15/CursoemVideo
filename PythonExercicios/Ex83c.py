frase = str(input('Digite uma expressão: ')).strip()

aberto = []
fechado = list()

for i in frase:

    if i == '(':
        aberto.append(i)

    elif i == ')':
        fechado.append(i)

if len(aberto) == len(fechado):
    print('A expressão está certa!')
else:
    print('Expressão Inválida!!')
