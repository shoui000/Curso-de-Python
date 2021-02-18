jooj = {}
jooj['nome'] = input('Nome do Jogador: ')
jooj['quantidade'] = int(input(f'Quantas partidas {jooj["nome"]} jogou: '))
jooj['gols'] = []
for a in range(0, jooj['quant']):
    jooj['gols'].append(int(input(f'Quantos gols {jooj["nome"]} fez na {a}ª partida: ')))
jooj['total'] = sum(jooj['gols'])
print('=' * 30)
print(jooj)
print('=' * 30)
for k, v in jooj.items():
    print(f'O campo {k} tem o valor {v}')
print('=' * 30)
print(f'O jogador {jooj["nome"]} jogou {jooj["quant"]} partidas')
for k, v in enumerate(jooj["gols"]):
    print(f'  => Na Partida {k}, fez {v} gols')
print(f'Foi um total de {jooj["total"]} gols')