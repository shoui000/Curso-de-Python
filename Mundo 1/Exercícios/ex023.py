'''num = str(input('Digite um milhar: '))
print('Unidades: {}'.format(num[3]))
print('Dezenas: {}'.format(num[2]))
print('Centenas: {}'.format(num[1]))
print('Milhares: {}'.format(num[0]))'''

num = int(input('Digite um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}'.format(num))
print('Unidades: '.format(u))
print('Dezenas: '.format(d))
print('Centenas: '.format(c))
print('Milhar: '.format(m))
