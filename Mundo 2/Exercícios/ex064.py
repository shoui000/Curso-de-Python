cont = 0
so = 0
fu = 0
while fu != 0:
    num = int(input('Digite um número: [999 para parar] '))
    if num == 999:
        fu = 1
    else:
        cont += 1
        so += num
print('Você digitou {} números e a soma entre eles foi {}'.format(cont, so))
