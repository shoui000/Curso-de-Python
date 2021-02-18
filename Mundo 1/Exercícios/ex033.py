a = float(input('Primeiro valor: '))
b = float(input('Segundo valor: '))
c = float(input('Terceiro valor: '))
# maior
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
# menor
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
        maior = c
print('O maior número é {}'.format(maior))
print('O menor número é {}'.format(menor))
