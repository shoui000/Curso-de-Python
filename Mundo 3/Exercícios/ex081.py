values = []
cinco = False
while True:
    a = int(input('Digite um valor: '))
    b = str(input('Continuará? [s/n]')).strip().upper()
    values.append(a)
    if b not in 'SN':
        while b not in 'SN':
            b = str(input('Continuará? [s/n]')).strip().upper()
    if b in 'N':
        break
values.sort(reverse=True)
print('-=-' * 10)
print(f'Foram digitados {len(values)} valores')
print(f'Os valores em ordem decresente: {values}')
if 5 in values:
    cinco = True
if cinco == True:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não faz parte da lista')
