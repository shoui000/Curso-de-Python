valores = []
posmaior = []
posmenor = []
maior = 0
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor na posição {c}: ')))
print('-=-'*20)
print(f'Os valores digitados foram: {valores}')
menor = valores[0]
posmenor.append(0)
for b, v in enumerate(valores):
    if v >= maior:
        if v == maior:
            posmaior.append(b)
        else:
            maior = v
            posmaior = []
            posmaior.append(b)
    elif v <= menor:
        if v == menor:
            posmenor.append(b)
        else:
            menor = v
            posmenor = []
            posmenor.append(b)
print(f'O maior valor digitado foi {maior} nas posições: {posmaior}')
print(f'O menor valor digitado foi {menor} nas posições: {posmenor}')
