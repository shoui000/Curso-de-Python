from time import sleep
print('\033[33m-=-\033[m' * 10)
print('    \033[1;36mCalculadora de médias\033[m')
print('\033[33m-=-\033[m' * 10)
med1 = float(input('\033[34mQual foi sua nota na primeira prova?\033[m '))
med2 = float(input('\033[34mQual foi sua nota na segunda prova?\033[m '))
media = (med1 + med2) / 2
print('\033[31mPROCESSANDO...\033[m')
sleep(1)
if media < 5.0:
    print('Sua média nessas duas provas foi \033[31m{:.2f}\033[m'.format(media))
    print('Você está \033[31mREPROVADO\033[m')
elif 5.0 <= media <= 6.9:
    print('Sua média nessas duas provas foi \033[34m{:.2f}\033[m'.format(media))
    print('Você está \033[34mde RECUPERAÇÃO\033[m')
elif media > 6.9:
    print('Sua média nessas duas provas fo \033[32m{:.2f}\033[m'.format(media))
    print('PARABÉNS! Você está \033[32mAPROVADO\033[m')
