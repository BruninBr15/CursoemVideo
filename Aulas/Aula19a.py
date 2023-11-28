filme = {
    'titulo': 'Star Wars IV: Uma Nova Esperança',
    'ano': 1977,
    'diretor': 'George Lucas'
}
print(filme.values())
print(filme.keys())
print(filme.items())
print(filme)
for k in filme.keys():
    print(k)
for v in filme.values():
    print(v)
for k, v in filme.items():
    print(f'O {k} é {v}')
