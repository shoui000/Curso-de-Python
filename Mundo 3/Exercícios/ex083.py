c = 0
d = 0
a = str(input('Digite uma expressão: ')).strip().split()
for b in a:
    if b == '(':
        c += 1
    if b == ')':
        d += 1
if c != d:
    print('Sua expressão está errada')
else:
    print('Sua expressão está valida')
