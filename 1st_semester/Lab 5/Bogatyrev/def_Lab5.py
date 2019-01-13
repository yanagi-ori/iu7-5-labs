eps = float(input('Введите точность: '))

print('\n' + '{:^15}'.format('Номер итерации') + ' |' + '{:^25}'.format('Текущий член ряда') + '|'
      + '{:^25}'.format('Текущее значение суммы'))
print('-'*16, '+', '-'*25, '+', '-'*23, sep='')
n = 0
z = 1
total = 4
denom = 3

while abs(z) > eps:
    n = n + 1
    z = (-1)**n * (1/denom)
    denom += 2
    total += 4 * z

print('Сумма ряда равна:', total)

