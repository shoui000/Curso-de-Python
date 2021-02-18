num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
while True:
    op = int(input('Digite um número de 0 a 20: '))
    while op < 0 or op > 20:
        op = int(input('Tente novamente! Digite um número de 0 a 20: '))
    print(f'Você digitou o número {num[op]}')
    continuar = str(input('Você quer fazer de novo? [S/N] ')).strip().upper()
    while continuar not in 'SN':
        continuar = str(input('Você quer fazer de novo? [S/N] ')).strip().upper()
    if continuar in 'N':
        break
