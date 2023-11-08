print('-=-'*10)
print('Análise de Triângulos')
print('-=-'*10)
l1 = int(input('Digite o tamanho de uma reta: '))
l2 = int(input('Digite o tamanho de outra reta: '))
l3 = int(input('Digite o tamanho de mais uma reta: \n'))
if l1 + l2 > l3 and l1 + l3 > l2 and l3 + l2 > l1:
    print('As 3 retas podem formar um triângulo.')
    if l1 == l2 and l1 == l3 and l3 == l2:
        print('Forma-se um triângulo equilátero!')
    elif l1 == l2 or l1 == l3 or l3 == l2:
        print('Forma-se um triângulo isósceles!')
    else:
        print('Forma-se um triângulo escaleno!')
else:
    print('NÃO forma um triângulo!')
