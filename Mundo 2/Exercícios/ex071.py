cin = vin = dez = um = 0
print('-=-' * 10)
print('{:^30}'.format('BANCO DA PRAÇA'))
print('-=-' * 10)
print('Temos notas de R$50.00, R$20.00, R$10.00 e R$1.00')
a = input('Agência: ')
b = input('Número da conta: ')
c = input('Senha: ')
din = int(input('Digite o valor a ser sacado: R$'))
while din != 0:
    if din >= 50:
        cin += 1
        din -= 50
    elif din >= 20:
        vin += 1
        din -= 20
    elif din >= 10:
        dez += 1
        din -= 10
    elif din >= 1:
        um += 1
        din -= 1
print('-=-' * 10)
if cin > 0:
    if cin > 1:
        print(f'Foram sacadas {cin} cédulas de R$50.00')
    elif cin == 1:
        print(f'Foi sacado 1 cédula de R$50.00')
if vin > 0:
    if vin > 1:
        print(f'Foram sacadas {vin} cédulas de R$20.00')
    elif vin == 1:
        print(f'Foi sacado 1 cédula de R$20.00')
if dez > 0:
    if dez > 1:
        print(f'Foram sacadas {dez} cédulas de R$10.00')
    elif dez == 1:
        print(f'Foi sacado 1 cédula de R$10.00')
if um > 0:
    if um > 1:
        print(f'Foram sacadas {um} moedas de R$1.00')
    elif um == 1:
        print(f'Foi sacado 1 moeda de R$1.00')
print('-=-' * 10)
print('Obrigado por utilizar o nosso serviço!')
