# import datetime
# help(print)
# help(datetime) obs.: pode ser usado direto no console, o que é melhor
# print(input.__doc__) 
# print(print.__doc__) obs.: tem a mesma função que o help() porém o help é mais completo


def contador(i, f, p):
    """
    ->  Faz uma contagem e mostra na tela
    :param i:   Ponto inicial da contagem
    :param f:   Ponto final da contagem
    :param p:   Passo da contagem
    :return:    Sem retorno
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('Fim')


help(contador)
