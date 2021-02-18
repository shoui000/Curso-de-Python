soma = mil = cont = menor = 0
menori = ''
print('-' * 31)
print('{:^31}'.format('LOJAS TABAJARA'))
print('-' * 31)
while True:
    nome = str(input('Produto: ')).strip()
    preco = float(input('Preço: R$'))
    if preco >= 1000:
        mil += 1
    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    soma += preco
    cont += 1
    if cont == 1 or preco < menor:
        menor = preco
        menori = nome
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continuar in 'N':
        break
print('-' * 7, 'FIM DO PROGRAMA', '-' * 7)
print(f'Foi gasto R${soma} nesta compra')
print(f'Foi um total de {mil} produtos valendo mais de R$1000.00')
print(f'O produto mais barato foi "{menori}" valendo R${menor}')
