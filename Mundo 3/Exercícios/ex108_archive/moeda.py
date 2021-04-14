def aumentar(n = 0, p = 0):
    p /= 100
    p = 1 + p
    return n * p

def diminuir(n = 0, p = 0):
    p /= 100
    p = 1 - p
    return n * p

def dobro(n = 0):
    return n*2

def metade(n = 0):
    return n/2

def moeda(p = 0, m = 'R$'):
    return f'{m}{p:.2f}'.replace('.',',')