# Богатырев Иван
# Интегралы


from sys import exit

from iu7_basemodule import easy_check


# Функция
def f(x):
    return x**2


# Интеграл через первообразную
def primitive(x):
    c = (x**3)/3
    return c


# Метод правых прямоугольников
def integral(x, y, n):
    h = (y - x) / n
    t = x + h
    result = 0
    for i in range(n):
        result += f(t)
        t += h
    result *= h
    return result


# Вычисление интеграла с заданной точностью
def rr_method(x, y):
    n = 1
    while abs(integral(x, y, 2 * n) - integral(x, y, n)) >= eps:
            n *= 2
    return integral(a, b, n), n


# Метод трех восьмых
def te_method(x, y, n):
    if n % 3 != 0:
        result = '-------'
    else:
        m = 3 * n - 1
        h = (y - x) / (3 * n)
        result = f(x) + f(y)
        for i in range(1, m):
            t = a + h * i
            if i % 3 == 0:
                result += 2 * f(t)
            else:
                result += 3 * f(t)
        result *= 3 * h / 8
        result = round(result, 7)
    return result


# Вычисление погрешностей
def anr_accuracy(x, itg):
    ab = abs(primitive(x) - itg)  # zero
    if primitive(x) == 0:
        print('На ноль делить нельзя\n(не удается вычислить '
              'относительную погрешность)')
        exit()
    re = abs((primitive(x) - itg) / primitive(x))
    return ab, re


not_te = False

a = easy_check(input('Введите начальное значение: '))
b = easy_check(input('Введите конечное значение: '))
n1 = int(easy_check(input('Введите первое количество участков разбиения: ')))
n2 = int(easy_check(input('Введиет второе количество участков разбиения: ')))
eps = easy_check(input('Введите значение точности: '))


int1 = integral(a, b, n1)
int2 = integral(a, b, n2)
if n1 % 3 != 0:
    int3 = '--------'
else:
    int3 = te_method(a, b, n1)
if n2 % 3 != 0:
    int4 = '--------'
else:
    int4 = te_method(a, b, n2)


print('\n1st method - Right rectangle method\n2nd method - 3/8 method')
print('-----------------------------------------------\n',
      '|   Name    |', '{:^16}|{:^16}'.format('1st n', '2nd n'), '|\n',
      '-----------------------------------------------\n',
      '| 1 method  |', '{:^16.7g}|{:^16.7g}'.format(int1, int2), '|\n',
      '-----------------------------------------------\n',
      '| 2 method  |', '{:^16}|{:^16}'.format(int3, int4), '|\n',
      '-----------------------------------------------', sep='')

ab1, re1 = anr_accuracy(a, int1)
ab2, re2 = anr_accuracy(a, int2)
if type(int3) == str:
    ab3, re3 = '--------', '--------'
else:
    ab3, re3 = anr_accuracy(a, int3)
    ab3, re3 = round(ab3, 7), round(re3, 7)
if type(int4) == str:
    ab4, re4 = '--------', '--------'
else:
    ab4, re4 = anr_accuracy(a, int4)
    ab4, re4 = round(ab4, 7), round(re4, 7)

# Вывод погрешностей в виде таблицы
print('\n\nCalculation errors\n-----------------------------------------------\n',
      '| Splittings |   Absolute    |    Relative    |\n',
      '-----------------------------------------------\n',
      '|{:^45}'.format('Right rectangles method'), '|\n'
      '-----------------------------------------------\n',
      '|    1st n   |{:^15.7g}|{:^15.7g}'.format(ab1, re1), ' |\n',
      '-----------------------------------------------\n'
      '|    2nd n   |{:^15.7g}|{:^15.7g}'.format(ab2, re2), ' |\n',
      '-----------------------------------------------\n',
      '|{:^45}'.format('3/8 method'), '|\n',
      '-----------------------------------------------\n',
      '|    1st n   |{:^15}|{:^15}'.format(ab3, re3), ' |\n',
      '-----------------------------------------------\n'
      '|    2nd n   |{:^15}|{:^15}'.format(ab4, re4), ' |\n',
      '-----------------------------------------------\n',
      sep='')

print('Integral with specified accuracy\n'
      'Value: {:9g}\n'
      'Number of splits: {}\n'
      'Accuracy: {}'.format(rr_method(a, b)[0],
                            rr_method(a, b)[1],
                            eps))
