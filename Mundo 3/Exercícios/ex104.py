algarismo = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
def leiaint(f, ff):
    ok = True
    while ok:
        n = input(f)
        if n.isnumeric():
            v = int(n)
            ok = False
        else:
            print(ff)
    return v


print(f'Você digitou o número {leiaint("Digite um número: ", "ERROR! Digite somente um número inteiro: ")}')