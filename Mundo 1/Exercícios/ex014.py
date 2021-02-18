c = float(input('Digite a temperatura em °C: '))
f = (c * (9/5)) + 32
k = c + 273.15
print('A temperatura é {:.1f}°C, {:.2f}°F e {:.2f}K!'.format(c, f, k))
