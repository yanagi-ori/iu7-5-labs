# Bogatyrev Ivan
# Infinite series
# eps - точность (эпсилон), step - шаг, x - значение x, iteration - количество повторений (итераций),
# n - номер итерации,


eps = float(input('Введите точность: '))
step = int(input('Введите шаг: '))
x = float(input('Введите значение x: '))
iteration = int(input('Введите кол-во итераций: '))
table_z = []
table_total = []
table_n = []

# Таблица
print('\n' + '{:^15}'.format('Номер итерации') + ' |' + '{:^25}'.format('Текущий член ряда') + '|'
      + '{:^25}'.format('Текущее значение суммы'))
print('-'*16, '+', '-'*25, '+', '-'*23, sep='')
n = total = 0
z = denom = 1
m = 2
grade = 3

while abs(z) > eps:
    while m < grade:
        denom *= m
        m += 2
    n = n + 1
    z = x**grade / (denom * grade)
    total += z
    grade += 2
    table_n.append(n)
    table_z.append(z)
    table_total.append(total)

for i in range(0, len(table_n), step):
    print('{:^15.7g}'.format(i + 1), '|', '{:^23.7g}'.format(table_z[i]),
          '|', '{:^23.13g}'.format(table_total[i]))
    print('-' * 16, '+', '-' * 25, '+', '-' * 23, sep='')

# Выводим причину, по которой цикл окончил работу.
if n >= iteration:
    print('\nПривышено максимальное число итераций')
elif abs(z) <= eps:
    print('Ряд сошелся')
