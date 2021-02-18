from datetime import date
print('\033[33m-=-\033[m' * 10)
print('  \033[36mAnalisador de Atletas\033[m')
print('\033[33m-=-\033[m' * 10)
year = int(input('\033[35mSe você é um nadador coloque aqui sua data de nascimento para saber sua categoria: \033[m'))
today = date.today().year
age = today - year
if age <= 9:
    print('Você tem {} anos e foi classificado como \033[34mMIRIM\033[m'.format(age))
elif 9 < age <= 14:
    print('Você tem {} anos e foi classificado como \033[34mINFANTIL\033[m'.format(age))
elif 14 < age <= 19:
    print('Você tem {} anos e foi classificado como \033[34mJÚNIOR\033[m'.format(age))
elif 19 < age <= 20:
    print('Você tem {} anos e foi classificado como \033[34mSÊNIOR\033[m'.format(age))
elif age > 20:
    print('Você tem {} anos e foi classificado como \033[34mMASTER\033[m'.format(age))
