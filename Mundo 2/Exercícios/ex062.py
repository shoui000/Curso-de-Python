p1 = float(input('Digite o primeiro termo de uma PA: '))
ra = float(input('Digite a razão de uma PA: '))
cont1 = p1
cont = 10
while cont > -1:
    if cont == 0:
        mais = int(input('Quer mostrar mais quantos termos (0 = sair): '))
        cont = mais
        if mais == 0:
            cont = cont -1
    else:
        if cont == 1:
            print(cont1)
        else:
            print(cont1, end='->')
        cont1 += ra
        cont = cont - 1
print('Acabou')
