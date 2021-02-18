flag = 1
cont = 0
maior = menor = num = 0
num2 = 0
while flag != 0:
    num = int(input('Digite um valor: '))
    num2 += num
    cont += 1
    if cont == 1:
        maior = menor = num
    elif num > maior:
        maior = num
    elif num < menor:
        menor = num
    mmm = str(input('Você quer continuar: [S/N] ')).upper().strip()[0]
    if 'N' in mmm:
        flag = 0
print('Você digitou {} números!'.format(cont))
print('A média deles ficou em {}'.format(num2 / cont))
print('O maior número digitado foi {} e o menor {}'.format(maior, menor))
