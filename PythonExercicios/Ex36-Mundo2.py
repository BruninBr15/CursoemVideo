valor_casa = float(input('Qual o valor da casa que o(a) senhor(a) deseja comprar?\n'))
salario = float(input('Informe qual o seu salário atual: '))
anos = int(input('Em quantos deseja pagar parcelar a casa?\n'))
prestacao = valor_casa/(anos*12)
print("="*25)
if prestacao < (salario * 0.3):
    print('Seu empréstimo foi aceito!\nO valor da prestação mensal vai fircar em R${:.2f}!'.format(prestacao))
else:
    print('A prestação ficaria em R${:.2f}. Seu empréstimo foi negado!'.format(prestacao))
    print('Tente parcelar em mais vezes.')
