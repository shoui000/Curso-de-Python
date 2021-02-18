from random import randint
pc = randint(0, 10)
pa = cont = soma = 0
pi = jogo = ''
while True:
    pa = int(input('Digite um número: '))
    pi = str(input('Você quer par ou ímpar: [P/I] ')).upper().strip()[0]
    soma = pa + pc
    if soma % 2 == 0:
        jogo = 'P'
    else:
        jogo = 'I'
    if jogo in pi:
        print('Você venceu!')
        cont += 1
    else:
        break
print(f'Você perdeu! Você ganhou {cont} partida(s) consecutiva(s)!')
