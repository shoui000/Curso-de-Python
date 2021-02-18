def maior(*num):
    print('-' * 30)
    print('Analisando os valores passados...')
    print('Valores: ', end='')
    for a in num:
        print(a, end=' ')
    print('')
    print(f'Foram informados {len(num)} ao total')
    for a, b in enumerate(num):
        if a == 0:
            maio = b
        else:
            if b > maio:
                maio = b
    if len(num) == 0:
        maio = 0
    print(f'Dos valores o maior é o {maio}')

maior(2, 9, 4, 5, 7, 1)

maior(4, 7, 0)

maior(1, 2)

maior(6)

maior()