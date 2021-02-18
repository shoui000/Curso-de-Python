algarismo = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
def leiaint(f, ff):
    lista = []
    v = input(f)
    while True:
        for l in v:
            if l not in algarismo:
                lista.append(l)
        if len(lista) > 0 or len(v) == 0:
            v = input(ff)
            lista = []
        else:
            break
    return v

    



print(f'Você digitou o número {leiaint("Digite um número: ", "ERROR! Digite somente um número: ")}')