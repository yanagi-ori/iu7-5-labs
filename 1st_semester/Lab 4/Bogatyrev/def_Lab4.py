from sys import exit


def func(yMax, yMin):
    return round((- yMin) / (yMax - yMin) * 70)


x0, xn, h = map(float, input("Введите x начальный, x конечный и шаг (через пробел): ").split())

if (x0 > xn and h >= 0) or (x0 < xn and h <= 0) or h == 0:
    exit('Недопустимые значения!')

print('{:>28}'.format('\nx начальный ='), '{:^5}'.format('{:.7g}'.format(x0)), sep='')
print('{:>28}'.format('x конечный ='), '{:^5}'.format('{:.7g}'.format(xn)), sep='')
print('{:>28}'.format('Шаг ='), '{:^5}'.format('{:.7g}'.format(h)), sep='')
print('+', '-'*15, '+', '-'*15, '+', sep='')
print('|', '{:^15}'.format('x'), '|', '{:^15}'.format('y'), '|', sep='')
print('+', '-'*15, '+', '-'*15, '+', sep='')

if x0 > xn:
    swap = x0
    x0 = xn
    xn = swap
    h *= -1

cur = min_f = x0
y_max = y_min = x0**2 + x0 - 6

while cur <= xn:
    z = cur**2 + cur - 6
    print('|', '{:^15}'.format('{:.7g}'.format(cur)), '|', '{:^15}'.format('{:.7g}'.format(z)), '|', sep='')
    print('+', '-' * 15, '+', '-' * 15, '+', sep='')
    if z > y_max:
        y_max = z
    if z < y_min:
        y_min = z
    cur += h
    if abs(z) < abs(min_f**2 - min_f - 6):
        min_f = cur

cur = x0
print('     {:4.2} {:>60.6}'.format(y_min, y_max))
while cur <= xn:
    y_cur = round((cur**2 + cur - 6 - y_min)/(y_max - y_min) * 70)
    print('{:>8g}'.format(round(cur, 10)), ' |', sep='', end='')
    i = 0
    if round(cur, 10) != 0:
        while i <= 70:
            if i == y_cur and i == func(y_max, y_min):
                print('+', end='')
            else:
                if i == y_cur: 
                    print('*', end='')
                elif i == round((- y_min)/(y_max - y_min)*70):
                    print('|', end='')
                else:
                    print(' ', end='')
            i += 1
    else:
        while i <= 70:
            if i == y_cur and i == round((- y_min)/(y_max - y_min)*70):
                print('+', end='')
            else:
                if i == y_cur:
                    print('*', end='')
                elif i == round((- y_min)/(y_max - y_min)*70):
                    print('|', end='')
                else:
                    print('-', end='')
            i += 1
    cur += h

    print(sep='')
