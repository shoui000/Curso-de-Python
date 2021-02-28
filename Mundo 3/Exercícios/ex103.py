def ficha(n='<desconhecido>', g=0):
    print(f'O jogador {n} fez {g} gols no campeonato.')

n = input('Nome do jogador: ')
g = input('Quantidade de gols: ')
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(g=g)
else:
    ficha(n, g)
    