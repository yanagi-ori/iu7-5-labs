x = float(input('Введите ваше x: '))
eps = float(input('Введите точность: '))
y = 0
curc = x
n = -1
summ = x
while abs(curc) > eps:
    n += 2
    curc = -curc * (x ** 2)/((n + 1) * (n + 2))
    summ += curc
    print('Элемент ', curc)
print('Сумма бесконечного ряда с точностью ', eps, ' = ', summ)