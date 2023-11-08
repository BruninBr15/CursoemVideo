frase = str(input('Digite uma frase: ')).strip()
print('A letra A aparece {} vezes ao todo!'.format(frase.lower().count('a')))
print('A primeira letra A fica na posição {} da frase;'.format(frase.lower().find('a') + 1))
print('A última letra A aparece na posição {} da frase.'.format(frase.rfind('a') + 1))
