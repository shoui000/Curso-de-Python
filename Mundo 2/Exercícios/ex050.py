soma = 0
cont = 0
for c in range(1, 7):
    a = int(input('Digite o {}º valor inteiro: '.format(c)))
    if a % 2 == 0:
        cont += 1
        soma += a
print('A soma de todos os \033[36m{}\033[m números {}PARES{} informados é {}{}{}'.format(
    cont, '\033[31m', '\033[m', '\033[36m', soma, '\033[m'))
