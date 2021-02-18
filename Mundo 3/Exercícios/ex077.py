palavras = ('alo', 'galerinha', 'do', 'youtube', 'eu', 'sou', 'o', 'dj', 'rogerinho')
vogais = ('a', 'e', 'i', 'o', 'u')
alao = []
cont = 0
for d in palavras:
    alao = []
    for c in vogais:
        if c in palavras[cont]:
            alao.append(c)
    print(f'A palavra {palavras[cont]} tem as seguintes vogais: {alao}')
    cont += 1
