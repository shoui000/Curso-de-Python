from math import hypot
num = float(input('Digite o comprimento do cateto oposto: '))
num2 = float(input('Digite o comprimeneto do cateto adjacente: '))
# num3 = (num ** 2 + num2 ** 2) ** (1/2)
# print('A hipotenusa mede {:.2f}'.format(num3))
num3 = hypot(num, num2)
print('A hipotenusa mede {:.2f}'.format(num3))