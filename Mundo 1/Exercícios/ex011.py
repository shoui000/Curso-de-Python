um = float(input('Qual é a largura da sua parede? '))
dois = float(input('Qual é a altura? '))
feijaocomarroiz = um*dois
print('Sua parede têm a dimensão de {}X{}, sendo {} m²'.format(um, dois, feijaocomarroiz))
print('Você precisará de {:.3f}L de tinta.'.format(feijaocomarroiz/2))
