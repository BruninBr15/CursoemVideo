nome = str(input('Qual é o seu nome?\n'))
if nome == 'Bruno':
    print('Que nome foda!')
elif nome == 'Anderson' or nome == 'Pedro':
    print('Seu nome me traz lembranças.')
elif nome in 'Gabriel Felipe João':
    print('Oi, irmão!')
else:
    print('Que nome normal.')
print('Prazer, {}!'.format(nome))
