cidad = str(input('Em que sua cidade você nasceu? ')).strip()
cidade = cidad.lower()
dividido = cidade.split()
tof = dividido[0]
if tof == 'santo':
    print('Sim, sua cidade começa com Santo')
else:
    print('Não, sua cidade não começa com Santo')
# print(cidade[:5] == 'santo')