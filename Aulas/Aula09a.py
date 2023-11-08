'''frase = str('Curso em Vídeo Python')
print(frase[9::3])
           [9:21:2]
           [9]
           [:9]
           [5:]'''
frase = 'Curso em Vídeo Python'
'''print(len(frase))
print(frase.count('o', 0, 13))
print(frase.find('Android'))
print('Curso' in frase)#Uma pergunta booleana, True or False
print(frase.replace('Python', 'HTML e CSS'))#Apesar de substituir, é temporário, na memória a variável
# ainda permanece com o primeiro valor atribuído a ela!
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())'''
dividido = frase.split()#Divide a string em mais 4 string's, e como aparece em [] no console, é uma lista.
#Essa lista tem um caractere pra cada palavra, nesse caso 4 caracteres(0, 1, 2, 3).
print(frase.upper().count('O'))
print(frase.upper().find('Vídeo'))
print(dividido[3][3])
print(len(frase))