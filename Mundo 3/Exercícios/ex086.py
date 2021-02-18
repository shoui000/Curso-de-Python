a = []
for b in range(0,9):
    a.append(float(input(f'Digite o {b + 1}º valor da matriz: ')))
print('-=-' * 10)
print('[{:^5}] [{:^5}] [{:^5}]'.format(a[0], a[1], a[2]))
print('[{:^5}] [{:^5}] [{:^5}]'.format(a[3], a[4], a[5]))
print('[{:^5}] [{:^5}] [{:^5}]'.format(a[6], a[7], a[8]))
