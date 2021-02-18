from random import randint
pc = randint(1, 10)
pl = 0
pa = 0
print('-=-' * 8)
print('Joguinho da adivinhação')
print('-=-' * 8)
print('Vou pensar em um número de 0 a 10, quero ver se você acertará!')
while pl != pc:
    pl = int(input('Digite seu palpite a seguir: '))
    pa += 1
    if pl < pc:
        print('Menos... Tente novamente!')
    elif pl > pc:
        print('Menos... Tente novamente!')
print('Parabéns você acertou!')
print('Você precisou de {} tentativas para acertar!'.format(pa))
