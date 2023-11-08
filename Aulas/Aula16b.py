lanches = ('Pastel', 'Suco', 'Esfiha', 'Pavê')  #No Python 3 pode tirar os parênteses da tupla.
print(lanches[0:2])

'''Tuplas são IMUTÁVEIS: 
lanches[1] = 'Refri' -> não é permitido
Só é possível alterá-la quando o programa estiver parado, iniciou não pode mexer.
'''

for comida in lanches:
    print(f'Vou comer {comida}.')
print('Tô de buchin chei!')
for cont, comida in enumerate(lanches):
    print(f'Vou comer {comida} que está na posição {cont}.')  #comida assumi um dos valores em lanches
print('Tô de buchin chei!')
for x in range(len(lanches)):
    print(f'Vou comer {lanches[x]} que está na posição {x}')
print('Tô de buchin chei!')

del lanches
print(lanches)
