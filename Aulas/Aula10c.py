import emoji
nome = str(input('Qual o seu nome?\n'))
if nome == 'Bruno':
    print('Que nome lindo!')
else:
    print('Que normal.', emoji.emojize('😐', language='alias'))
print('Bom dia, {}!'.format(nome))
