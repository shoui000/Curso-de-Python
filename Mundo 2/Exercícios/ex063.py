um = 0
dois = 1
treis = 0
n = int(input(':: '))
print(um, end='->')
print(dois, end='->')
while n > 0:
    treis = um + dois
    print(treis, end='->')
    um = dois
    dois = treis
    n = n - 1
print('Acabou')
