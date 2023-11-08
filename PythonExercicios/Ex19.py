from random import choice
n1 = str(input('Informe o primeiro aluno: '))
n2 = str(input('Informe o segundo aluno: '))
n3 = str(input('Informe o terceiro aluno: '))
n4 = str(input('Informe o quarto aluno: '))
lista = [n1, n2, n3, n4]
sorteado = choice(lista)
print('O sorteado para apagar o quadro foi {}!'.format(sorteado))
