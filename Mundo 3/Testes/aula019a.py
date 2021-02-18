pessoa = {'nome': 'Gustavo', 'idade': 22, 'sexo': 'Masculino'}
print(f'O {pessoa["nome"]} tem {pessoa["idade"]} anos')

print(pessoa.keys())

print(pessoa.values())

print(pessoa.items())

for k, v in pessoa.items():
    print(f'{k} = {v}')

del pessoa["sexo"]
pessoa['nome'] = "pica"
pessoa["peso"] = 900

for k, v in pessoa.items():
    print(f'{k} = {v}')