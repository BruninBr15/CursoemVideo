'''
teste = list()
teste.append('Pedro')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = '19'
galera.append(teste[:])
print(galera)'''
galera = list()
dado = list()
maior = menor = 0
for x in range(0, 3):
    dado.append(str(input('Nome: ').strip()))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()  #Se não limpar, ele vai repetir o primeiro e segundo item. p[0] e p[1] vão ser os mesmos sempre.
print(galera)
for p in galera:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade.')
        maior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        menor += 1
print(f'{maior} são maiores e {menor} são menores.')
