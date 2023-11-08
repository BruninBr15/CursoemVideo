soma = 0
cont = 0
for x in range (1,500,2):
    if x % 3 == 0:
        soma = soma + x
        cont = cont + 1
print('A soma de todos os {} números ímpares e múltiplos de 3 entre 1 e 500 é {}!'.format(cont, soma))
