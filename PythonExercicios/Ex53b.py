frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]#começa do início, terminar no fim, de trás pra frente
print('O inverso de {} é {}.'.format(junto, inverso))
if inverso == junto:
    print('A frase É um palíndromo!')
else:
    print('A frase NÃO é um palíndromo!')