nome = str(input('Qual o seu nome?\n')).strip().split()
print('Seu primeiro nome é {}!'.format(nome[0]))
print('Seu último nome é {}!'.format(nome[len(nome) - 1]))#len em Bruno Avelino Cavalcante conta 3, mas no split vai até
# 2, por isso eu mostro isso menos 1 na lista.
