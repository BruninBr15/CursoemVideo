frase = str(input('Digite uma expressão: ')).strip()

parenteses = []

for i in frase:

    if i == '(':
        parenteses.append(i)

    elif i == ')':
        if len(parenteses) > 0:
            parenteses.pop()

        else:
            parenteses.append(i)

if len(parenteses) == 0:
    print('Todos os parênteses foram fechados!')
else:
    print('Expressão inválida!')
