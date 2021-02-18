times = ('Flamengo', 'Palmeiras', 'Santos', 'São Paulo', 'Internacional', 'Corinthians',
 'Grêmio', 'Bahia', 'Athletico-PR', 'Goiás', 'Vasco da Gama', 'Atlético', 'Botafogo',
 'Fortaleza', 'Ceará SC', 'Fluminense', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')
print('-=-' * 30)
print(f'A tabela: {times}')
print('-=-' * 30)
print(f'O G5 do Brasileirão atual é: {times[:5]}')
print('-=-' * 30)
print(f'Os times {times[16:]} estão no Z4')
print('-=-' * 30)
print(f'Os times da série A em ordem alfabética: {sorted(times)}')
print('-=-' * 30)
print(f'A Chapecoense está em {times.index("Chapecoense") + 1}º lugar na tabela')
print('-=-' * 30)
