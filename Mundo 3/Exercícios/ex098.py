from time import sleep
def contador(i, f, p=1):
    print('-' * 30)
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.2)
            cont += p
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.2)
            cont -= p
    print('Fim')
    print('-' * 30)
    sleep(0.2)

contador(1, 10)

contador(10, 0, 2)

print('Agora é a sua vez de personalizar a contagem!')

contador(i = int(input('Início: ')), f= int(input('Fim: ')), p= int(input('Passo: ')))