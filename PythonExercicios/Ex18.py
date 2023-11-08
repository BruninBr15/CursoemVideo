from math import cos, sin, tan, radians
a = float(input('Digite um ângulo: '))
a = radians(a)
cos = cos(a)
sen = sin(a)
tan = tan(a)
print('Seno {:.2f}, cosseno {:.2f} e tangente do ângulo {:.2f}.'.format(sen, cos, tan, a))
