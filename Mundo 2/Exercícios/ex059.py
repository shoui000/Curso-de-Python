op1 = 0
num1 = float(input('Digite um valor: '))
num2 = float(input('Digite outro valor: '))
num3 = 0
igual = 0
maior = 0
menor = 0
sair = 0
while sair == 0:
    print('-==-' * 11)
    print('Digite a seguir o número da opção desejada: ')
    print('[1] - Somar')
    print('[2] - Multiplicar')
    print('[3] - Comparar')
    print('[4] - Novos Números')
    print('[5] - Sair')
    op1 = int(input('>>>>> Opção: '))
    print('-==-' * 11)
    if op1 == 1:
        num3 = num1 + num2
        print('O resultado da operação é {}'.format(num3))
    elif op1 == 2:
        num3 = num1 * num2
        print('O resultado da operação é {}'.format(num3))
    elif op1 == 3:
        if num2 < num1:
            maior =  num1
            menor = num2
        elif num2 > num1:
            maior = num2
            menor = num1
        elif num2 == num1:
            igual = 1
        if igual == 1:
            print('Os dois números são iguais')
        else:
            print('O maior número é {} e o menor é {}'.format(maior, menor))
    elif op1 == 4:
        num1 = float(input('Digite um valor: '))
        num2 = float(input('Digite outro valor: '))
    elif op1 == 5:
        sair = 1
    else:
        print('Opção inexistente')
