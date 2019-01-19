from math import sin


def func(x):
    return sin(x)



def integrate(x, y, n):

    c = 0
    t = 0

    step = (y-x)/n
    result = func(a) + func(b)
    for i in range(1, n):
        c += func(i)
    c *= 2
    result += c

    i = 0.5
    while i < n:
        t += func(i)
        i += 1
    t *= 4
    result += t
    result = result * step / 6
    return result




# Ввод переменных
a = float(input('Введите начальное значение: '))
b = float(input('Введите конечное значение: '))
n = int(input('Введите кол-во участков: '))

result = integrate(a, b, n)

print('{:8g}'.format(result))