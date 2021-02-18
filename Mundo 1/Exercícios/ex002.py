msg = str(input("What's your name? ")).strip()
print('Hello {}{}{}! Nice to meet you!'.format('\033[0;36m', msg, '\033[m'))
