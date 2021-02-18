from time import sleep
from datetime import date
ano = date.today().year
print('\033[33m-=-\033[m' * 20)
print("                   \033[36mAlistamento Militar\033[m")
print('\033[33m-=-\033[m' * 20)
born = int(input('\033[34mQual é o ano de seu nascimento?\033[m'))
dif = ano - born
print('\033[31mPROCESSANDO...\033[m')
sleep(2)
if dif == 18:
    print('\033[35mEsta na hora de se alistar no exército. Parabéns Soldado!\033[m')
elif dif > 19:
    print('\033[35mVocê deveria ter se alistado! Já se passou {} anos!\033[m'.format((dif - 18)))
elif dif <= 18:
    print('\033[35mAproveite, porque faltam {} anos para o \033[1;35mGRANDE DIA\033[m\033[m'.format((18 - dif)))
