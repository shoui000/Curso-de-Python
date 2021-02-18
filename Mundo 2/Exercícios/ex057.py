flag = 0
while flag != 1:
    sexo = str(input('Digite seu sexo: [M/F]')).strip().upper()[0]
    if sexo in 'MmFf':
        flag = 1
    else:
        print('Dados invalidos. Tente novamente')
print('Sexo {} registrado com sucesso!'.format(sexo))
