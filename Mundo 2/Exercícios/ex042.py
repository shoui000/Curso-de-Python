print('\033[33m-=-\033[m' * 10)
print('\033[36mAnalisador de Triângulos\033[m')
print('\033[33m-=-\033[m' * 10)
print('\033[35mDigite a seguir três segmentos de reta e informaremos a você:\033[m')
print('- Se podem ou não formar um triângulo;')
print('- Se é um triângulo\033[34m equilátero, isósceles ou escaleno;\033[m')
r1 = float(input('\033[35mPrimeiro segmento:'))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento:\033[m '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print('Os segmentos acima \033[34mPODEM\033[m formar um triângulo')
    if r1 == r2 and r2 == r3:
        print('Os segmentos apresentados formam um triângulo \033[34mEQUILÁTERO\033[m')
    elif r1 == r2 and r2 != r3:
        print('Os segmentos apresentados formam um triângulo \033[34mISÓSCELES\033[m')
    elif r2 == r3 and r2 != r1:
        print('Os segmentos apresentados formam um triângulo \033[34mISÓSCELES\033[m')
    elif r1 == r3 and r1 != r2:
        print('Os segmentos apresentados formam um triângulo \033[34mISÓSCELES\033[m')
    elif r1 != r2 != r3:
        print('Os segmentos apresentados formam um triângulo \033[34mESCALENO\033[m')
else:
    print('Os segmentos acima \033[31mNÃO PODEM\033[m formar um triângulo')
