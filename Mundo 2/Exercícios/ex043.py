print('\033[33m-=-\033[m' * 10)
print('\033[36mCalculadora de IMC\033[m')
print('\033[33m-=-\033[m' * 10)
height = float(input('\033[35mDigite sua altura em metros: \033[m'))
weight = float(input('\033[35mDigite seu peso em quilos: \033[m'))
imc = height ** 2 / weight
if imc < 18.5:
    print('Seu IMC está em {}')
    print('Você está\033[31m abaixo\033[m do seu peso ideal!')
    print('Procure já um nutricionista para se informar mais!')
elif imc >= 18.5 < 25:
    print('Seu IMC está em {}'.format(imc))
    print('Você está em seu peso\033[32m ideal\033[m')
elif imc >= 25 < 30:
    print('Seu IMC está em {}')
    print('Você está\033[31m acima\033[m do seu peso ideal!')
    print('Procure um nutricionista para se informar mais!')
elif imc >= 30 < 40:
    print('Seu IMC está em {}')
    print('Você está\033[31m com obesidade\033[m')
    print('Procure um nutricionista já para se informar mais!')
elif imc <= 40:
    print('Seu IMC está em {}')
    print('Você está\033[31m com obesidade morbida\033[m')
    print('Procure um nutricionista já para se informar mais!')
