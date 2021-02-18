from random import randint
i = (randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9))
print(f'Os números sorteados foram: ', end='')
for a in i:
    print(f'{a}', end=' ')
print(f'\nO maior número foi: {max(i)}')
print(f'O menor número foi: {min(i)}')
