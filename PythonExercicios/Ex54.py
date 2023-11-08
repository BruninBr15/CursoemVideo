from datetime import date
nasc = []
atual = date.today().year
idade = 0
menores = 0
maiores = 0
for x in range(0,7):
    nasc.append(int(input('Qual o ano de nascimento da {}º pessoa?\n'.format(x+1))))
    idade = atual - nasc[x]
    if idade < 18:
        menores = menores + 1
    else:
        maiores = maiores + 1
print('Dessas pessoas {} são menores de idade e {} são maiores.'.format(menores, maiores))
