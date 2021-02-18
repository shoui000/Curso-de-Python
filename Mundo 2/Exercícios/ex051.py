prim = int(input('Primeiro termo: '))
raz = int(input('Razão: '))
décimo = prim + (10 - 1) * raz
for c in range(prim, décimo + raz, raz):
    print('{} '.format(c), end='->')
print('Acabou')
