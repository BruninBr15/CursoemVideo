#n = bool(input('Digite um valor: '))
#print(n)
# Como eu defini a varável como booleana, o valor é True quando tem um número e False quando não tem.
n = input('Digite algo: ')
print('O tipo primitivo desse valor é ', type(n))
print('É um número?',n.isnumeric())
print('É alfabético? ',n.isalpha())
print('Tem alfabeto e número? ', n.isalnum())
print('Está em maiúsculo? ', n.isupper())
print('Está em minúsculo? ', n.islower())
print('Está capitalizada? ', n.istitle())
# O a é um objeto, portanto tem características e funcionalidades, atributos e métodos. No caso, como tem parênteses,
# estão sendo trabalhados os métodos.
