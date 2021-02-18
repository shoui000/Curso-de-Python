from time import sleep
print('\033[0;33m-=-\033[m' * 20)
print('            \033[1;36mPrograma finaciador de casas\033[m')
print('\033[0;33m-=-\033[m' * 20)
house = float(input('\033[1;34mQual é valor da casa?\033[m '))
money = float(input('\033[1;34mQual é sua renda mensal?\033[m '))
time = float(input('\033[1;34mEm quantos meses você gostaria de pagar?\033[m '))
print('\033[1;31mPROCESSANDO...\033[m')
sleep(3)
if house / time <= (money * 0.30):
    print('O seu finaciamento está de acordo com as regras da Caixa Econômica Federal')
    print('As prestações estão avaliadas em {}{:.2f}{} reais'.format('\033[0;35m', house / time, '\033[m'))
elif house / time >= (money * 0.30):
    print('O seu finaciamento não está de acordo com as regras da Caixa Econômica Federal')
    print('Infelizmente o senhor terá que ou aumentar as pretações ou conseguir uma renda maior')
else:
    print('Algo deu errado')
    print('Tente novamente')
