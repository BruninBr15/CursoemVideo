frase = str(input('Digite uma expressão: ')).strip()

aberto = frase.count('(')

fechado = frase.count(')')

if aberto == fechado:
    print('Todos os parênteses foram fechados.')
else:
    print('Expressão inválida!')
