from random import randint
from time import sleep
pc = randint(0, 3)
print('\033[31m-=-\033[m' * 5)
print('\033[32m    JOKENPÔ\033[m')
print('\033[31m-=-\033[m' * 5)
print('\033[35mDigite o número da opção desejada:\033[m')
print('\033[31m[0]\033[m - Pedra')
print('\033[31m[1]\033[m - Papel')
print('\033[31m[2]\033[m - Tesoura')
pe = float(input(' '))
print('\033[35mPROCESSANDO...\033[m')
sleep(2)
if pe == pc:
    print('\033[31m-=-\033m' * 10)
    print('\033[32mEMPATE\033[m')
    print('Tente novamente, talvez você ganhe!')
    print('\033[31m-=-\033m' * 10)
elif pe == 1 and pc == 0 or pe == 2 and pc == 1 or pe == 0 and pc == 2:
    print('\033[31m-=-\033m' * 10)
    print('\033[36mPARABÉNS\033[m, você ganhou!')
    print('\033[31m-=-\033m' * 10)
elif pe == 0 and pc == 1 or pe == 2 and pc == 0 or pe == 1 and pc == 2:
    print('\033[31m-=-\033m' * 10)
    print('\033[31mPERDEDOR\033[m')
    print('Tente novamente, talvez você ganhe!')
    print('\033[31m-=-\033m' * 10)
