from time import sleep
def escre(txt):
    a = len(txt) + 4
    print('~' * a)
    print('  {}'.format(txt), flush=False)
    print('~' * a)

while True:
    escre('Sistema de Ajuda PyHelp')
    a = input('Função ou Biblioteca >>> ')
    if a == 'fim':
        escre('TABOM ENTÃO')
        break
    escre(f'Acessando o manual do comando "{a}"')
    sleep(0.3)
    print(help(a))
    
