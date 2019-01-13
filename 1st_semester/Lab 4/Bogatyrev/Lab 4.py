# Лабораторная работа 4
# Богатырев Иван
#
# x0 - х начальный
# xn - x конечный
# h - шаг
# z = a**7 - a**6 + 8*a**5 - 4*a**4 + 6*a**3 + 2*a**2 - 5*a + 1
# cur - x в цикле

from sys import exit
x0, xn, h = map(float, input("Введите x начальный, x конечный и шаг (через пробел): ").split())

if (x0 > xn and h >= 0) or (x0 < xn and h <= 0) or h == 0:
    exit('Недопустимые значения!')

# Общие данные
print('{:>28}'.format('\nx начальный ='), '{:^5}'.format('{:.7g}'.format(x0)), sep='')
print('{:>28}'.format('x конечный ='), '{:^5}'.format('{:.7g}'.format(xn)), sep='')
print('{:>28}'.format('Шаг ='), '{:^5}'.format('{:.7g}'.format(h)), sep='')
print('+', '-'*15, '+', '-'*15, '+', sep='')
print('|', '{:^15}'.format('x'), '|', '{:^15}'.format('y'), '|', sep='')
print('+', '-'*15, '+', '-'*15, '+', sep='')

# Перестановка, если обратный порядок
if x0 > xn:
    swap = x0
    x0 = xn
    xn = swap
    h *= -1

cur = min_f = x0
y_max = y_min = x0**7 - x0**6 + 8*x0**5 - 4*x0**4 + 6*x0**3 + 2*x0**2 - 5*x0 + 1

while cur <= xn:
    z = cur**7 - cur**6 + 8*cur**5 - 4*cur**4 + 6*cur**3 + 2*cur**2 - 5*cur + 1
    print('|', '{:^15}'.format('{:.7g}'.format(cur)), '|', '{:^15}'.format('{:.7g}'.format(z)), '|', sep='')
    print('+', '-' * 15, '+', '-' * 15, '+', sep='')
    if z > y_max:
        y_max = z
    if z < y_min:
        y_min = z
    cur += h
    if abs(z) < abs(min_f ** 7 - min_f ** 6 + 8 * min_f ** 5 - 4 * min_f ** 4 +
                    6 * min_f ** 3 + 2 * min_f ** 2 - 5 * min_f + 1):
        min_f = cur

cur = x0
print('     {:4.2} {:>60.6}'.format(y_min, y_max))
while cur <= xn:
    y_cur = round((cur**7 - cur**6 + 8*cur**5 - 4*cur**4 + 6*cur**3 + 2*cur**2 - 5*cur + 1
                   - y_min)/(y_max - y_min) * 70)
    print('{:>8g}'.format(round(cur, 10)), ' |', sep='', end='')
    i = 0
    if round(cur, 10) != 0:
        while i <= 70:
            if i == y_cur:
                print('*', end='')
            elif i == round((- y_min)/(y_max - y_min)*70):
                print('|', end='')
            else:
                print(' ', end='')
            i += 1
    else:
        while i <= 70:
            if i == y_cur:
                print('*', end='')
            elif i == round((- y_min)/(y_max - y_min)*70):
                print('|', end='')
            else:
                print('-', end='')
            i += 1

    print(sep='')
    cur += h
