print('-='*15)
print('10 TERMOS DE UMA P.A.')
print('-='*15)

primeiro = int(input('Digite o primeiro termo da P.A.: '))
razao = int(input('Digite a razão: '))
decimo = primeiro + (10-1) * razao

print('-'*11)

for x in range(primeiro, (decimo+1), razao):

    print(x, end=' ')
