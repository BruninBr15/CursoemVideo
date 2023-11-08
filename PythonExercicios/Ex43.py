peso = float(input('Informe o seu peso em kg: '))
altura = float(input('Informe a sua altura em m: '))
imc = peso /(altura**2)
print('Seu IMC é {:.1f}.\n'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO do peso ideal! Ganhe um pouco mais de massa.')
elif imc >= 18.5 and imc < 25:
    print('Você está com o PESO IDEAL!')
elif imc >= 25 and imc < 30:
    print('Você está com SOBREPESO! Cuidado.')
elif imc >= 30 and imc < 40:
    print('Você está com OBESIDADE! Procure uma nutricionista.')
else:
    print('Você está com OBESIDADE MÓRBIDA! Você corre riscos, procure um especialista.')

