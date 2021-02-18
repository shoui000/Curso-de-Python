al = {}
al['Nome'] = str(input('Nome: '))
al['Média'] = float(input('Média: '))
while al['Média'] > 10 or al['Média'] < 0:
    al['Média'] = float(input('ERROROROROROR! Média: '))
if al['Média'] >= 7:
    al['Situação'] = 'Aprovado'
else:
    al['Situação'] = 'Reprovado'
for k, v in al.items():
    print(f'{k} é igual a {v}')