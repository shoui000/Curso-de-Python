a = (int(input('Digite um valor: ')), int(input('Digite um 2º valor: ')), int(input('Digite um 3º valor: ')), int(input('Digite o 4º e último valor: ')))
h = [0]
print(f'Os valores digitados foram: {a}')
print(f'O número 9 apareceu {a.count(9)} vezes')
if 3 in a:
    print(f'O número 3 apareceu pela primeira vez na {a.index(3)+1}ª posição')
else:
    print('O número 3 não apareceu nenhuma vez')
print('Os números pares são: ', end='')
for g in a:
    print(g, end=' ')
