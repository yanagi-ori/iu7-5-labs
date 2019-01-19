from math import sin, cos
def function(x):
    return sin(x)

def tochnoeI(a, b):
    return (-cos(b) + cos(a))

def integral1(a, b, n):

    result = 0
    step = (b-a) / n

    for i in range(n):
        result += function(a + step * (i + 0.5))
    result *= step
    return result

def integral10(a,b,n):
    result = 0
    step = (b - a) / n

    for i in range(n):
        if abs(integral1(a,b,2*n)-integral1(a,b,n)) > eps:
            result += function(a + step * (i + 0.5))
    result *= step
    return result


def integral2(a, b, n):
    m = 3*n - 1
    step = (b - a) / (3*n)

    result = function(a) + function(b)

    for i in range(1, m):
        x = a + step * i
        if i % 3 == 0:
            result = result + 2 * function(x)
        else:
            result = result + 3 * function(x)
    result = 3 * result * step / 8
    return result

a, b = map(float, input('Введите a, b: ').split())
n1, n2 = map(int, input('Введите первое и второе кол-во итераций: ').split())
eps = float(input('Введите точность: '))

integrall1 = integral10(a, b, n1)
integrall2 = integral2(a, b, n1)
integrall3 = integral10(a, b, n2)
integrall4 = integral2(a, b, n2)






print('1 метод - серединных перпендекуляров')
print('2 метод - 3/8')
print('┏━'+'━'*77+'┓')
print('┃      Ваш метод      ┃     1-ое n:', '{:5}'.format(n1),'   ┃'
              '    2-ое n:', '{:5}'.format(n2), '    ┃')
print('━'* 79)
print('┃       Метод 1       ┃', '{:^20.8g}'.format(integrall1),'┃'
              '', '{:^20.8g}'.format(integrall3), '┃')
print('━'* 79)
print('┃       Метод 2       ┃', '{:^20.8g}'.format(integrall2),'┃'
              '', '{:^20.8g}'.format(integrall4), '┃')
print('┗'+'━'*77+'┛')
print()
print('Абсолютная погрешность - ', '{:.8g}'.format(abs(tochnoeI(a,b) - integrall1)))
print('Относительная погрешность - ','{:.8g}'.format(abs((tochnoeI(a,b) - integrall1)/tochnoeI(a,b))))
