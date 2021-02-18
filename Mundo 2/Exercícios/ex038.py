from time import sleep
print('\033[0;33m-=-\033[m' * 20)
print('        \033[0;35mPrograma comparador de números inteiros\033[m')
print('\033[0;33m-=-\033[m' * 20)
num = int(input('\033[34mDigite um número inteiro:\033[m '))
num2 = int(input('\033[34mDigite outro número inteiro:\033[m '))
print('\033[31mPROCESSANDO...\033[m')
sleep(2)
if num > num2:
    print('O número {}{}{} é \033[1mMAIOR\033[m do que o número {}{}{}'.format(
        '\033[36m', num, '\033[m', '\033[36m', num2, '\033[m'))
elif num < num2:
    print('O número {}{}{} é \033[1mMENOR\033[m do que o número {}{}{}'.format(
        '\033[36m', num, '\033[m', '\033[36m', num2, '\033[m'))
elif num == num2:
    print('Não tem nem um menor nem um maior')
    print('Porque os número são \033[1;36mIGUAIS\033[m')
else:
    print('Algo deu errado')
    print('Por Favor tente novamente')
