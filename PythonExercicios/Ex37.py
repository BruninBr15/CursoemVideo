n = int(input('Digite um número: '))
print('''1 - para converter pra BINÁRIO!
2 - para converter pra OCTAL!
3 - para converter pra HEXADECIMAL!''')
escolha = int(input('Qual conversão você deseja fazer?\n'))
print('-=-'*20)
if escolha == 1:
    print('{} convertido para BINÁRIO é {}.'.format(n, bin(n)[2:]))
elif escolha == 2:
    print('{} convertido para OCTAL é {}.'.format(n, oct(n)[2:]))
elif escolha == 3:
    print('{} convertido para HEXADECIMAL é {}.'.format(n, hex(n)[2:]))
else:
    print('NÚMERO INVÁLIDO!')
