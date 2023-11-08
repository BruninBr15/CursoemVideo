n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input('Digite a sua segunda nota: '))
media = (n1 + n2)/2
print('As notas do primeiro e segundo trimestre do aluno, respectivamente, são {:.1f} e {:.1f}.\n'.format(n1, n2))
if media >= 0 and media < 5:
    print('A média das notas é {:.1f}. O aluno está REPROVADO!'.format(media))
elif media >= 5 and media < 6.9:
    print('A média das notas é {:.1f}. O aluno está de RECUPERAÇÃO!'.format(media))
elif media >= 7 and media <= 10:
    print('A média das notas é {:.1f}. O aluno está APROVADO!'.format(media))
else:
    print('NOTA INVÁLIDA!')
