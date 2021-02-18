from random import choice
um = input('Digite o nome do primeiro aluno dos quatro: ')
dois = input('Digite o nome do segundo aluno dos quatro: ')
feijaocomarroiz = input('Digite o nome do terceiro aluno dos quatro: ')
tres = input('Digite o nome do quarto aluno dos quatro: ')
quatro = [um, dois, feijaocomarroiz, tres]
feijaonoprato = choice(quatro)
print('O escolhido foi {}!!!'.format(feijaonoprato))
