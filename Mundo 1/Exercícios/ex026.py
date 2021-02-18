frase = input('Digite uma frase: ').strip().lower()
count = frase.count('a')
dd = frase.find('a') + 1
ee = frase.rfind('a') + 1
print('Na sua frase aparece {} vezes a letra A!'.format(count))
print('Na frase a letra A apareceu  na {}ª posição'.format(dd))
print('Na frase a letra A apareceu na {}ª posição'.format(ee))
