def resumo(n = 0, p1 = 10, p2 = 10):
    print('-' * 30)
    print('{:^30}'.format('Resumo do Valor'))
    print('-' * 30)
    print(f'Preço Analisado: \t{moeda(p=n)}')
    print(f'Dobro do Preço: \t{dobro(n, True)}')
    print(f'Metade do Preço: \t{metade(n, True)}')
    print(f'{p1}% do Aumento: \t{aumentar(n, p1, True)}')
    print(f'{p2}% do Redução: \t{diminuir(n, p2, True)}')
    print('-' * 30)
    

def resumocnt():
    return

def aumentar(n = 0, p = 0, m=False):
    p /= 100
    p = 1 + p
    if m:
        resu = n * p
        return moeda(p=resu)
    else:
        return n * p

def diminuir(n = 0, p = 0, m=False):
    p /= 100
    p = 1 - p
    if m:
        resu = n * p
        return moeda(p=resu)
    else:
        return n * p

def dobro(n = 0, m=False):
    if m:
        resu = n*2
        return moeda(p=resu)
    else:
        return n*2

def metade(n = 0, m=False):
    if m:
        resu = n/2
        return moeda(p=resu)
    else:
        return n/2

def moeda(p = 0, m = 'R$'):
    return f'{m}{p:.2f}'.replace('.',',')