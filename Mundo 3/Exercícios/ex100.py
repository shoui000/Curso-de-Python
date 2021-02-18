from random import randint
def sorteio(lista):
    for a in range(0, 5):
        lista.append(randint(1, 10))
    print(f'Sorteando 5 valores da lista: {lista}')

def somapa(lista):
    b = 0
    for a in lista:
        if a % 2 == 0:
            b += a
    print(f'Somando os valores pares de {lista}: temos {b}')

lista = []

sorteio(lista)

somapa(lista)
