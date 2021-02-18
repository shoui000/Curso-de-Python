dias = int(input('Por quantos dias ele foi alugado? '))
km = float(input('Quantos KM rodados? '))
preco = (dias * 60) + (km * 0.15)
print('Total a pagar: R${:.2f}'.format(preco))
