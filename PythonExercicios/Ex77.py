palavras = ('Tigre',
            'Eleonora',
            'Limlisha',
            'Tetia',
            'Ludmila',
            'Sofia')

for word in palavras:

    print(f'\nO nome {word.upper()} tem as vogais: ', end='')

    for letter in word:

        if letter.lower() in 'aeiou':
            print(letter.lower(), end=' ')
