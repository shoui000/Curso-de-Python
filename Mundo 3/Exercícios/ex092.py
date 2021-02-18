from datetime import datetime
dados = {}
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho: '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de Contratação: '))
    dados['salario'] = float(input('Salário: '))
    dados['aposentadoria'] = (dados['contratação'] + 35) - nasc
print('-=-' * 10)
for k, v in dados.items():
    print(f'  -- O {k} tem o valor {v}')
