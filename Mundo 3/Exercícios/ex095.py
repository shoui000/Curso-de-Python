jogall = []
jog = {}
while True:
    print('-=-' * 10)
    jog['nome'] = input('Nome do Jogador: ')
    jog['quant'] = int(input(f'Quantas partidas {jog["nome"]} jogou: '))
    jog['quantall'] = []
    jog['total'] = 0
    for b in range(0, jog['quant']):
        jog['quantall'].append(int(input(f'Quantos gols ele fez na partida {b}: ')))
    for b in jog['quantall']:
        jog['total'] += b
    jogall.append(jog.copy())        
    a = input('Quer continuar? [S/N] ')
    while a.lower() not in 'sn':
        a = input('Quer continuar? [S/N] ')
    if a.lower() in 'n':
        break
print('-=-' * 20)
print('cod nome                gols          total')
print('-' * 46)
for b, c in enumerate(jogall):
    print('{:<4}{:<20}{:<14}{:<8}'.format(b, c['nome'], str(c['quantall']), c['total']))
print('-' * 46)
print('-=-' * 20)
while True:
    g = int(input('Mostrar dados de qual jogador: '))
    if g == 999:
        break
    while g > len(jogall) or g < 0:
        g = int(input('Mostrar dados de qual jogador: '))
    else:
        print('-=-' * 20)
        print(f'-- LEVANTAMENTO do jogador {jogall[g]["nome"]}')
        for l, k in enumerate(jogall[g]['quantall']):
            print(f'    No jogo {l} fez {k} gols')
        print('-=-' * 20)
