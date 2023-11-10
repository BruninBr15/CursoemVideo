num = list()

for x in range(0, 5):

    num.append(int(input('Digite um número: ')))

print('<>'*16)

print(f'O MAIOR valor foi {max(num)} na posição {num.index(max(num))+1}ª')

print(f'O MENOR valor foi {min(num)} na posição {num.index(min(num))+1}º')
