n = c = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    else:
        c += n
print(c)