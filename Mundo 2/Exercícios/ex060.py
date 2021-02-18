'''from math import factorial
fact = int(input('Digite um número para saber seu fatorial: '))
print('O fatorial de {} é {}'.format(fact, factorial(fact)))'''

n = int(input('Digite um número para saber seu fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))
