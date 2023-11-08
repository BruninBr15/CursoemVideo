print('='*25)
print('Loja Python')
print('='*25)
preco = float(input('Digite o preço total das compras: '))
print('''As formas de pagamento são: 
1 - Pagamento à vista em dinheiro
2 - Pagamento à vista no cartão
3 - 2x no cartão
4 - 3x ou mais no cartão''')
pag = int(input('Qual a forma de pagamento?\n'))
print('')
if pag == 1:
    print('Sua compra vai receber 10% de desconto, e vai custar R${}!'.format(preco*0.9))
elif pag == 2:
    print("Sua compra vai receber 5% de desconto, e vai custar R${}!".format(preco*0.95))
elif pag == 3:
    print('As duas parcelas da sua compra vão custar R${} cada!'.format(preco/2))
elif pag == 4:
    juros = preco * 1.2
    parcelas = int(input('Pretende dividir em quantas vezes?\n'))
    print('Sua compra irá receber JUROS!\nDe R${} vai passar a ser R${:.2f}.\nParcelado em {}x cada parcela vai custar R${:.2f}!'.format(preco, juros, parcelas, (juros/parcelas)))
