from random import randint
from time import sleep
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5 tente adivinhar...')
print('-=-' * 20)
usuario = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(3)
if usuario == randint(0, 5):
    print('UAU, você adivinhou!!')
else:
    print('Infelizmente não foi desta vez. ;-;')
