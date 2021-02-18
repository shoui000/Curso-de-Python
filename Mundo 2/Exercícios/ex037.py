print('\033[33m-=-\033[m' * 10)
print('\033[34m     Conversor de Números\033[m')
print('\033[33m-=-\033[m' * 10)
num = int(input('Digite o valor que queira converter: '))
print('''Escolha a seguir uma base para conversão: 
\033[34m[0]\033[m - BINÁRIO
\033[34m[1]\033[m - OCTAL
\033[34m[2]\033[m - HEXADECIMAL''')
option = int(input('\033[35mOpção:\033[m '))
if option == 0:
    print('\033[34m{}\033[m convertido para \033[36mBINÁRIO\033[m fica como \033[34m{}\033[m'.format(num, bin(num)[2:]))
elif option == 1:
    print('\033[34m{}\033[m convertido para \033[36mOCTAL\033[m fica como \033[34m{}\033[m'.format(num, oct(num)[2:]))
elif option == 2:
    print('\033[34m{}\033[m convertido para \033[36mHEXADECIMAL\033[m fica como \033[34m{}\033[m'.format(num, hex(num)[2:]))
else:
    print('\033[31mOPÇÃO ERRADA\033[m')
