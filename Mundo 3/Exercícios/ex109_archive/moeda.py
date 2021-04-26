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