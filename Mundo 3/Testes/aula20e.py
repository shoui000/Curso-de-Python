def dobra(lst):
    for a in range(0, len(lst)):
        lst[a] *= 2

lista = [1, 2, 3]
dobra(lista)
print(lista)