# Operadores (), ** , * , / , // , % , - , +.
# '='*20   print('='*20)
# nome = input('Qual o seu nome?\n')
# print('Prazer em te conhecer {:=^20}!'.format(nome))
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1 + n2
su = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
p = n1 ** n2
print('A soma entre eles é {}, \na subtração é {}, \na multiplicação é {},\n'.format(s, su, m), end='')
print('A divisão é {:.2f}, \na divisão inteira é {} \ne a potência é {}.'.format(d, di, p))