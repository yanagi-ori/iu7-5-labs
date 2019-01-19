from math import factorial
x = float(input('Введите ваше x: '))
eps = float(input('Введите точность: '))
y = 0
curc = 1
n = 0
summ = x
while abs(curc) > eps:
    n += 2
    curc = curc *(x*x) *(2*n-1)*2/(2*n*(2*n+1))
    summ += curc
    print('Элемент ', curc)
    print('Сумма ', summ)
print('Сумма бесконечного ряда с точностью ', eps, ' = ', summ)