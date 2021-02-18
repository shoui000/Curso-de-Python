km = float(input('Digite a velocidade do seu carro: '))
if km > 80:
    print('Você está acima da velocidade máxima e por isso foi multado')
    acima = (km - 80) * 7
    print('A sua multa está avaliada em {:.2f} reais'.format(acima))
elif km == 80:
    print('Cuidado você está no máximo da velocidade, mais pouco você pode ser multado!')
else:
    print('Tenha um bom dia! Dirija com segurança!')
