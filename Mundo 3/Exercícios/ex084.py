dados = []
galera = []
pesados = []
leves = []

while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    galera.append(dados[:])
    dados.clear()
    cont = str(input('Quer continuar? [S/N] ')).strip().upper()
    while cont not in 'SN':
        cont = str(input('Tente novamente. Quer continuar? [S/N] ')).strip().upper()
    if cont in 'N':
        break

print('-=-' * 10)

for a, b in enumerate(galera):
    if a == 0:
        pesados.append(b)
        leves.append(b)
    else:
        if b[1] > pesados[0][1]:
            pesados.clear()
            pesados.append(b)
        elif b[1] == pesados[0]:
            pesados.append(b)
        elif b[1] < leves[0][1]:
            leves.clear()
            leves.append(b)
        elif b[1] == leves[0][1]:
            leves.append(b)

print(f'Ao todo, você cadastrou {len(galera)} pessoas')
print(f'O maior peso foi de {pesados[0][1]}Kg. Peso de ', end='')
for a in pesados:
    print(a[0], end=' ')
print()
print(f'O menor peso foi de {leves[0][1]}Kg. Peso de ', end='')
for a in leves:
    print('[', a[0], ']', end=' ')
print()
print('-=-' * 10)
