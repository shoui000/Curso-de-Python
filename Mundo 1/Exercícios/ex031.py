km = float(input('Digite a distância em km do seu local até o destino: '))
# preco = km * 0.50 if km <= 200 else km * 0.45
if km <= 200:
    preco = km * 0.5
    print('A passagem está avaliada em {:.2f} reais'.format(preco))
else:
    preco = km * 0.45
    print('A passagem está avaliada em {:.2f} reais'.format(preco))
