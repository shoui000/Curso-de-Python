def area(lar, alt):
    print(f'A área de um terreno {lar} x {alt} é de {lar * alt}m²')

print('Controle de Terrenos')
print('-' * len('Controle de Terrenos'))
area(lar= float(input('Largura (m): ')), alt= float(input('Altura (m): ')))
