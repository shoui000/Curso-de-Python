values = []
while True:
    a = int(input('Digite um valor: '))
    if a in values:
        print('Valor duplicado! Não vai ser adicionado!')
    elif a not in values:
        print('Valor adicionado com sucesso!')
        values.append(a)
    continues = str(input('Vai querer continuar?[s/n] ')).strip().upper()
    if continues not in 'SN':
        while continues not in 'SN':
            continues = str(input('Tente novamente! Vai querer continuar?[s/n] ')).strip().upper()
    if continues in 'N':
        break
print('-=-' * 20)
print(f'Você digitou os valores: {sorted(values)}')
