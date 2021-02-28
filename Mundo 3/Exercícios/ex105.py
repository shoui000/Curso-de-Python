def notas(* notas, sit=False):
    """
    -> programa que analisa as notas recebidas
    :param notas: todas as notas 
    :param sit:    (opcional) mostra ou não a situação do aluno
    :param return:  retorna um dicionario com as informações
    """
    dic = {}

    dic['total'] = len(notas)
    dic['maior'] = max(notas)
    dic['menor'] = min(notas)

    media = sum(notas)/len(notas)

    dic['média'] = float('{:.2f}'.format(media))

    if sit:
        if dic['média'] >= 8:
            dic['situação'] = 'Boa'
        elif dic['média'] > 5:
            dic['situação'] = 'Razoável'
        elif dic['média'] < 5:
            dic['situação'] = 'Ruim'
    
    return dic

print(notas())