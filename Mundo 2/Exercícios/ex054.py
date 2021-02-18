from datetime import date
maior = 0
menor = 0
ano = date.today().year
for c in range(1, 8):
    pessoa = int(input('Ano de nascimento da {}ª pessoa: '.format(c)))
    idade = ano - pessoa
    if idade >= 21:
        maior += 1
    elif idade < 21:
        menor += 1
print('Foram registradas {} pessoas maiores de idade'.format(maior))
print('e {} pessoas menores de idade'.format(menor))
