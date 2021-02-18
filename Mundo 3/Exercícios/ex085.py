a = []
b = []
c = [a, b]
for d in range(0, 7):
    e = int(input(f'Digite o \033[36m{d + 1}º\033[m valor: '))
    if e % 2 == 0:
        a.append(e)
    else:
        b.append(e)
print('-=-' * 10)
print('Números \033[36mpares\033[m digitados em ordem crescente: ', end='')
print('\033[34m', sorted(a), '\033[m')
print('Números \033[36mímpares\033[m digitados em ordem crescente: ', end='')
print('\033[34m', sorted(b), '\033[m')
