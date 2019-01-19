# Склифасовский Денис ИУ-7 15Б
# Программа, которая считает интеграл 2 разными методами
# 1 метод - метод серединных прямоугольников
# 2 метод - метод трех восьмых
from math import sin, cos


# Проверка на дурака
def test(x):
    x.strip()
    while x.lstrip('-').replace('.', '', 1)\
            .replace('e-', '', 1).replace('e+', '', 1)\
            .replace('e', '',1).isdigit() == False:
        x = input('Ошибка, введите число еще раз: ')
    x = float(x)
    return x


# Наща функция
def func(x):
    return sin(x)


# Интеграл, используя первообразную
def accuracy(x, y):
    c = -cos(x)+cos(y)
    return c


# Интеграл без точности
def integral(x, y, n):
    result = 0
    step = (y - x) / n
    for i in range(n):
        c = x + step * (i + 0.5)
        result += func(c)
    result *= step
    return result


# Интеграл с точностью до эпсилона
def integral2(x, y, n):
    result = 0
    step = (y - x) / n
    for i in range(n):
        if abs(integral(a, b, 2 * n) - integral(a, b, n)) < eps:
            c = a + step * (i + 0.5)
            result += func(c)
        result *= step
    return result


# Метод трех восьмых
def integral3(x, y, n):
    m = 3 * n - 1
    step = (y - x) / (3 * n)
    result = func(x) + func(y)
    for i in range(1, m):
        t = a + step * i

        if i % 3 == 0:
            result = result + 2 * func(t)
        else:
            result = result + 3 * func(t)
    result = 3 * result * step / 8
    return result


# Ввод переменных
a = input('Введите начальное значение: ')
a = test(a)
b = input('Введите конечное значение: ')
b = test(b)
n1 = input('Введите первое кол-во участков: ')
n1 = test(n1)
n1 = int(n1)
n2 = input('Введите второе кол-во участков: ')
n2 = test(n2)
n2 = int(n2)
eps = input('Введите точность: ')
eps = test(eps)


# Подсчет интегралов
in1 = integral2(a, b, n1)
in2 = integral3(a, b, n1)
in3 = integral2(a, b, n2)
in4 = integral3(a, b, n2)


# Вывод методов
print('1 метод - серединных прямоугольников')
print('2 метод - 3/8')


# Вывод в виде таблицы
print('┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓')
print('┃ Ваш метод ┃ 1-ое n: {:^5} ┃ 2-ое n: {:^5} ┃'.format(n1, n2))
print('┃    1-ый   ┃{:^15.7g}┃{:^15.7g}┃'.format(in1, in3))
print('┃    2-ой   ┃{:^15.7g}┃{:^15.7g}┃'.format(in2, in4))
print('┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛')

        
# Нахождение абсолютной и относительной точностей 1-ого кол-ва разбиений
ab1 = abs(accuracy(a, b) - in1)
ot1 = abs((accuracy(a, b) - in1)/accuracy(a, b))


# Нахождение абсолютной и относительной точностей 2-ого кол-ва разбиений
ab2 = abs(accuracy(a, b) - in2)
ot2 = abs((accuracy(a, b) - in2)/accuracy(a, b))

print()
'''
# Вывод этих точностей для 1-ого кол-ва разбиений
print('Для кол-ва разбиений = ', n1)
print('Абсолютная - {:7g}'.format(ab1))
print('Относительная - {:7g}'.format(ot1))

print()

# Вывод этих точностей для 2-ого кол-ва разбиений
print('Для кол-ва разбиений = ', n2)
print('Абсолютная - {:7g}'.format(ab2))
print('Относительная - {:7g}'.format(ot2))
'''

# Вывод погрешностей в виде таблицы
print('┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓')
print('┃ Разбиения ┃   Абсолютная  ┃ Относительная ┃')
print('┃  1-ое n   ┃{:^15.7g}┃{:^15.7g}┃'.format(ab1, ot1))
print('┃  2-ое n   ┃{:^15.7g}┃{:^15.7g}┃'.format(ab2, ot2))
print('┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛')
