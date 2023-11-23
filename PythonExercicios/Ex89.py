ficha = []

while True:
    nome = str(input('Nome do aluno: '))

    nota1 = float(input('1ª nota: '))

    nota2 = float(input('2ª nota: '))

    media = (nota1 + nota2) / 2

    ficha.append([nome, [nota1, nota2], media])

    resp = str(input('Deseja continuar (S/N)?\n')).strip().upper()[0]
    if resp == 'S':
        continue
    else:
        break

print()
print('Nº\t\tNOME\t\tMÉDIA')
print('_'*30)

for i, aluno in enumerate(ficha):
    print(f'{i}\t\t{aluno[0]}\t\t{aluno[2]:.2f}')

while True:
    print('_'*30)

    i_aluno = int(input('De qual aluno você deseja checar as notas (999 para parar)?\n'))

    if i_aluno == 999:
        break

    else:
        print(f'As duas notas de {ficha[i_aluno][0]} são: {ficha[i_aluno][1]}')

print('PROGRAMA FINALIZADO!! Volte sempre!')
