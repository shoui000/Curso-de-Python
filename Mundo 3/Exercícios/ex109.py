from ex109_archive import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {p} é {moeda.metade(p, m=True)}')
print(f'O dobro de {p} é {moeda.dobro(p, m=True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10, m=True)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(p, 13, m=True)}')