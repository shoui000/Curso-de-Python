a = []
for b in range(0,9):
    a.append(float(input(f'Digite o {b + 1}º valor da matriz: ')))
print('-=-' * 10)
print('[{:^5}] [{:^5}] [{:^5}]'.format(a[0], a[1], a[2]))
print('[{:^5}] [{:^5}] [{:^5}]'.format(a[3], a[4], a[5]))
print('[{:^5}] [{:^5}] [{:^5}]'.format(a[6], a[7], a[8]))
print('-=-' * 10)
d = 0
for b in a:
    if b % 2 == 0:
        d += b
print(f'A soma de todos os valores pares é: {d}')
e = a[2] + a[5] + a[8]
print(f'A soma de todos os valores da terceira coluna: {e}')
f = [a[3], a[4], a[5]]
for z, b in enumerate(f):
    if z == 0:
        m = b
    else:
        b < m
        m = b
print(f'O maior valor da segunda linha: {m}')
