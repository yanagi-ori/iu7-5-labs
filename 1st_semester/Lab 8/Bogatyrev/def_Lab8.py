from iu7_basemodule import easy_check


def f(x):
    return x**2


def primitive(x):
    c = (x**3)/3
    return c


def simpson_method(a, b, n):
        h = (b-a)/n
        k = 0.0
        x = a + h
        for i in range(1, int((n/2 + 1))):
            k += 4 * f(x)
            x += 2 * h
        x = a + 2 * h
        for i in range(1, int(n/2)):
            k += 2 * f(x)
            x += 2 * h
        result = (h/3) * (f(a) + f(b) + k)
        result = round(result, 7)
        return result


def te_method(x, y, n):
        m = 3 * n - 1
        h = (y - x) / (3 * n)
        result = f(x) + f(y)
        for i in range(1, m):
            t = x + h * i
            if i % 3 == 0:
                result += 2 * f(t)
            else:
                result += 3 * f(t)
        result *= 3 * h / 8
        result = round(result, 7)
        return result


def anr_accuracy(x, itg):
    ab = abs(primitive(x) - itg)  # zero
    if primitive(x) == 0:
        print('На ноль делить нельзя\n(не удается вычислить '
              'относительную погрешность)')
        exit()
    re = abs((primitive(x) - itg) / primitive(x))
    return ab, re


a = easy_check(input('Введите начальное значение: '))
b = easy_check(input('Введите конечное значение: '))
n1 = int(easy_check(input('Введите первое количество участков разбиения: ')))
n2 = int(easy_check(input('Введиет второе количество участков разбиения: ')))

if n1 % 2 != 0:
    int1 = '--------'
else:
    int1 = simpson_method(a, b, n1)
if n2 % 2 != 0:
    int2 = '--------'
else:
    int2 = simpson_method(a, b, n2)
if n1 % 3 != 0:
    int3 = '--------'
else:
    int3 = te_method(a, b, n1)
if n2 % 3 != 0:
    int4 = '--------'
else:
    int4 = te_method(a, b, n2)

print('\n1st method - Simpson method method\n2nd method - 3/8 method')
print('-----------------------------------------------\n',
      '|   Name    |', '{:^16}|{:^16}'.format('1st n', '2nd n'), '|\n',
      '-----------------------------------------------\n',
      '| 1 method  |', '{:^16}|{:^16}'.format(int1, int2), '|\n',
      '-----------------------------------------------\n',
      '| 2 method  |', '{:^16}|{:^16}'.format(int3, int4), '|\n',
      '-----------------------------------------------', sep='')


if type(int1) == str:
    ab1, re1 = '--------', '--------'
else:
    ab1, re1 = anr_accuracy(a, int1)
    ab1, re1 = round(ab1, 6), round(re1, 6)

if type(int2) == str:
    ab2, re2 = '--------', '--------'
else:
    ab2, re2 = anr_accuracy(a, int2)
    ab2, re2 = round(ab2, 6), round(re2, 6)

if type(int3) == str:
    ab3, re3 = '--------', '--------'
else:
    ab3, re3 = anr_accuracy(a, int3)
    ab3, re3 = round(ab3, 6), round(re3, 6)

if type(int4) == str:
    ab4, re4 = '--------', '--------'
else:
    ab4, re4 = anr_accuracy(a, int4)
    ab4, re4 = round(ab4, 7), round(re4, 7)


print('\n\nCalculation errors\n-----------------------------------------------\n',
      '| Splittings |   Absolute    |    Relative    |\n',
      '-----------------------------------------------\n',
      '|{:^45}'.format('Right rectangles method'), '|\n'
      '-----------------------------------------------\n',
      '|    1st n   |{:^15}|{:^15}'.format(ab1, re1), ' |\n',
      '-----------------------------------------------\n'
      '|    2nd n   |{:^15}|{:^15}'.format(ab2, re2), ' |\n',
      '-----------------------------------------------\n',
      '|{:^45}'.format('3/8 method'), '|\n',
      '-----------------------------------------------\n',
      '|    1st n   |{:^15}|{:^15}'.format(ab3, re3), ' |\n',
      '-----------------------------------------------\n'
      '|    2nd n   |{:^15}|{:^15}'.format(ab4, re4), ' |\n',
      '-----------------------------------------------\n',
      sep='')