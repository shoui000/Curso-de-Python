a = []
b = []
while True:
    b.append(str(input('Nome do aluno: ')))
    c = float(input('Nota da 1ª prova: '))
    if c > 10 or c < 0:
        c = float(input('ERROR! Nota da 1ª prova: '))
    b.append(c)
    if c > 10 or c < 0:
        c = float(input('ERROR! Nota da 2ª prova: '))
    b.append(c) 
    a.append(b[:])
    b.clear()
    c = str(input('Quer continuar? [s/n] ')).strip().upper()
    while len(c) < 1 or c not in 'SN':
        c = str(input('Tente novamente! Quer continuar? [s/n] ')).strip().upper()
    if c in 'N':
        break
print('-=-' * 10)
for e, d in enumerate(a):
    if e == 0 :
        print('{:^30}'.format('Nº - Nome - Nota 1 - Nota 2'))
        print(f'[{e}] - {d[0]} .......... {d[1]} .. {d[2]}')
    else:
        print(f'[{e}] - {d[0]} .......... {d[1]} .. {d[2]}')
while True:
    g = int(input('De qual criança quer ver a média? [-1 para cancelar] '))
    if g == -1:
        break
    print(f'Nome: {a[g][0]}')
    print(f'Nota 1: {a[g][1]}')
    print(f'Nota 2: {a[g][2]}')
    p = (a[g][1] + a[g][2]) / 2
    print(f'Média: {p}')
    if p < 6:
        print(f'O {a[g][0]} está\033[31m Reprovado\033[m')
    else:
        print(f'O {a[g][0]} está \033[32mAprovado\033[m')