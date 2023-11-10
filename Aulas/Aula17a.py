lista = ['Tigre', 'Eleonora', 'Ludmila']

'''del lista[1]
lista.pop(1)
lista.pop()  #Remove o último elemento
if 'Tigre' in lista:
    lista.remove('Tigre')  #Remove pelo conteúdo, não pela chave, ou índice'''

valores = list(range(4, 11))  #Cria uma lista de 0 até 6 com valores do 4 até o 10 (o 11 não entra).

a = [0, 5, 8, 3, 7, 2, 5]
#b = a  Cria uma ligação entre a e b
b = a[:]  #Pega todos os elementos de a e passa pro b

a.sort()  #Coloca em ordem crescente
a.sort(reverse=True)  #Em ordem decrescente
print(sorted(a))  #Neste comando, a lista vai aparecer ordenada.

lista.append('Lim')
lista.insert(1, 'Tetia')

for k,x in enumerate(lista):
    print(f'Na posição {k+1} está {x}!')
print('ACABOU!')
