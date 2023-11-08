nome = str(input('Qual o seu nome completo?\n')).strip()
print('Seu nome em maiúsculo é: {};'.format(nome.upper()))
print('Seu nome em minúsculo é: {};'.format(nome.lower()))
print('Seu nome tem ao todo {} letras;'.format(len(nome)-nome.count(' ')))#Contar quantos espaços no nome e tirar
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
primeiro_nome = nome.split()
print('Seu primerio nome, {}, tem {} letras.'.format(primeiro_nome[0], len(primeiro_nome[0])))
