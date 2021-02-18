person = {}
a = ''
b = 0
molieres = []
acima = []
people= []

while True:
    person['nome'] = input('Nome: ')
    person['sexo'] = input('Sexo [m/h]: ')
    while person['sexo'] not in 'mh':
        person['sexo'] = input('Sexo [m/h]: ')
    person['idade'] = int(input('Idade: '))
    people.append(person.copy())
    a = input('Adicionar mais pessoas [s/n]: ')
    while a.lower() not in 'sn':
        a = input('Adicionar mais pessoas [s/n]: ')
    if a in 'n':
        break

print('=*=' * 10)

print(f'Foram {len(people)} pessoas cadastradas')
for c in people:
    b += c['idade']
b = b / len(people)
print(f'A média de idade das pessoas cadastradas é {b}')
for c in people:
    if c['sexo'].lower() in 'm':
        molieres.append(c)

print('=*=' * 10)

print('Todas as mulheres: ')
for c in molieres:
    print(c['nome'])

print('=*=' * 10)

for c in people:
    if c['idade'] >= b:
        acima.append(c)

print('Todas as pessoas com a idade acima da média das cadastradas')

for c in acima:
    print(c['nome'])
