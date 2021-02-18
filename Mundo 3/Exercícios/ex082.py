c = []
d = []
e = []
while True:
    a = int(input('Digite um número: '))
    b = str(input('Quer continuar? [s/n] ')).strip().upper()
    while b not in 'SN':
        b = str(input('Tente Novamente: Quer continuar? [s/n] ')).strip().upper()
    if a % 2 == 0:
        c.append(a)
    elif a % 2 != 0:
        d.append(a)
    e.append(a)
    if b in 'N':
        break
print('-=-' * 10)
print(f'Todos os números: {e}')
print(f'Números pares: {c}')
print(f'Números Impares: {d}')
