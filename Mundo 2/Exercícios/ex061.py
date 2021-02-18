p1 = float(input('Digite o primeiro termo de uma PA: '))
ra = float(input('Digite a razão de uma PA: '))
cont1 = p1
cont = 10
while cont > 0:
    if cont == 1:
        print(cont1)
    else:
        print(cont1, end='->')
    cont1 += ra
    cont -= 1
print('Acabou')
