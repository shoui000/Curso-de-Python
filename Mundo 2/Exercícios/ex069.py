f = m = i = c = 0
while True:
    print('-=-' * 10)
    print('{:^30}'.format('CADASTRO DE PESSOAS'))
    print('-=-' * 10)
    nome = input('Nome: ')
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Sexo: [M/F] ')).upper().strip()[0]
    idade = int(input('Idade: '))
    continuar = ' '
    while continuar not in 'SN':
        print('-=-' * 10)
        continuar = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
    c += 1
    if sexo in 'F' and idade < 20:
        f += 1
    elif sexo in 'M':
        m += 1
    if idade >= 18:
        i += 1
    if continuar in 'N':
        break
print('-=-' * 10)
print(f'Foram digitadas {c} pessoas;')
print(f'Delas, {f} são mulheres com menos de 20 anos;')
print(f'{m} são homens;')
print(f'{i} são maiores de 18 anos.')
print('-=-' * 10)
