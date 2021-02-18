s = float(input('Digite o valor do salário do funcionário: R$'))
if s > 1250.00:
    a = s * 1.10
else:
    a = s * 1.15
print('O seu salário com aumento é igual a {:.2f} reais'.format(a))