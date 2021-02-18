def ficha(n, g):
    if len(n) == 0 and len(g) == 0:
        n = '<desconhecido>'
        g = 0
    print(f'O jogador {n} fez {g} gols no campeonato')

ficha(n=input('Nome do Jogador: '), g=str(input('Quantidade de gols: ')))