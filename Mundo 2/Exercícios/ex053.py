oi = str(input('Digite sua frase: ')).strip().upper()
palavras = oi.split()
junto = ''.join(palavras)
inverso = junto[::-1]
'''for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]'''
if inverso == junto:
    print('Temos Um palíndromo')
else:
    print('Não temos um palíndromo')
