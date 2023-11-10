'''
dados = list()
pessoas = []
dados.append('Pedro')
dados.append(25)
pessoas.append(dados[:])
print(len(pessoas))
print(dados)
'''
pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]]
print(pessoas[2][0])
