from datetime import date
def voto(a):
    idade = date.today().year - a
    if idade >= 16 and idade < 18 or idade >= 60:
        return 'Opcional'
    elif idade < 16:
        return 'Negado'
    else:
        return 'Obrigatório'

a = int(input('Ano de nascimento: '))
print(f'A pessoa tem voto {voto(a)}')
