from random import randint
lista = []
cont = 0
listaa = []
op = int(input('Quantos palpites você quer: '))
for a in range(0, op):
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    cont = 0
    if lista not in listaa:
        listaa.append(lista[:])
        lista.clear()
    else:
        lista.clear()
        op + 1
print('Todos os palpites: ')
for b in listaa:
    print(b)
