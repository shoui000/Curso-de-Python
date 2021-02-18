def fatorial(num, show=False):
    """
    Faz o fatorial de um numero
    :param n: Numero inicial
    :param show: (opcional) Mostrar ou não a conta
    :return: nenhum retorno
    """
    a = 1
    c = ''
    for b in range(1, num+1):
        a *= b
        if show and b != num:
            c = f'{c}{b} x '
        elif show and b == num:
            c = f'{c}{b} = '
    c = f'{c}{a}'
    return c

    

print(fatorial(5, True))