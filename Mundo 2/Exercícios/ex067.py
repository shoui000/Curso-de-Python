while True:
    tabu = float(input('Quer ver a tabuada de qual valor? [-1 para parar] '))
    if tabu < 0:
        break
    print('-' * 30)
    for a in range(1, 11):
        print(f'{tabu} x {a} = {tabu * a}')
    print('-' * 30)
print('Fim')
