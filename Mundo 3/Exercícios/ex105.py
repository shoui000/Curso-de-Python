def notas(* notas, sit=False):
    """
    -> programa que analisa as notas recebidas
    :*notas: todas as notas 
    :sit:    (opcional) mostra ou não a situação do aluno
    :return:  retorna um dicionario com as informações
    """
    dic = {}
    maior = 0
    menor = 0
    media = 0

    dic['total'] = len(notas)

    for a, b in enumerate(notas):
        if a == 0:
            maior = b
            menor = b
        else:
            if b > maior:
                maior = b
            if b < menor:
                menor = b
    
    dic['maior'] = maior
    dic['menor'] = menor

    for a in notas:
        media += a

    media /= len(notas)

    dic['média'] = float('{:.2f}'.format(media))

    if sit:
        if dic['média'] >= 8:
            dic['situação'] = 'Boa'
        elif dic['média'] < 7 and dic['média'] > 5:
            dic['situação'] = 'Razoável'
        elif dic['média'] < 5:
            dic['situação'] = 'Ruim'
    
    return dic

print(notas())