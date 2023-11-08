'''cidade = str(input('Informe em qual cidade você nasceu: ')).strip().capitalize().split()
print('Santo' in cidade[0])'''
cidade = str(input('Em qual cidade você mora?\n')).strip()
print(cidade[:5].capitalize() == 'Santo')
