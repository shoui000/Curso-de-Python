from random import shuffle
um = input('Primeiro aluno: ')
dois = input('Segundo aluno: ')
feijaocomarroiz = input('Terceiro aluno: ')
tres = input('Quarto aluno: ')
quatro = [um, dois, feijaocomarroiz, tres]
shuffle(quatro)
print('A ordem de apresentação é: ')
print(quatro)
