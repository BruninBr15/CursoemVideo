''' ceil = arredondamento pra cima
    floor = arredondamento pra baixo
    trunc = truncamento, eliminar da vírgula
    pow = potência
    sqrt = raíz quadrada
    factorial = fatorial
    '''
from math import sqrt, floor
n = int(input('Digite um número inteiro: '))
raiz = sqrt(n)
print('A raíz de {} = {}!'.format(n, floor(raiz)))
