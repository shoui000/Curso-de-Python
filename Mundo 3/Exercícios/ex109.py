from ex109_archive import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {p} é R${moeda.moeda(moeda.metade(p, m=True))}')
print(f'O dobro de {p} é R${moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando 10%, temos R${moeda.moeda(moeda.aumentar(p, 10))}')
print(f'Reduzindo 13%, temos R${moeda.moeda(moeda.diminuir(p, 13))}')