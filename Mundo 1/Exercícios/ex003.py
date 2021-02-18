um = int(input('Digite um numero: '))
dois = int(input('Digite outro numero: '))
feijaocomarroiz = um + dois
# print('A soma entre', um, 'e', dois, "é igual a", feijaocomarroiz)
print('A soma entre {}{}{} e {}{}{} é igual a {}{}{}.'.format('\033[0;33m', um, '\033[m', '\033[0;33m', dois, '\033[m',
                                                              '\033[0;36m', feijaocomarroiz, '\033[m'))
