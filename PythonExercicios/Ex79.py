num = list()

while True:

    n = int(input('Digite um número: '))
    if n not in num:  #Só será adicionado se não estiver na lista
        num.append(n)
    else:
        print('Valor já digitado! Por favor, digite outro número!')

    resp = str(input('Quer adicionar mais valores? (S/N)\n')).strip().upper()[0]
    if resp == 'N':
        break

print('<>'*17)

num.sort()

print('Os valores digitados são:', end=' ')
for x in num:
    print(x, end=' ')
