#Сусликов Д. ИУ7-15б
# Защита суммы последовательности

eps = float(input('Введите точность '))
maks = float(input('Введите максимальное число итераций '))
s = 1
n = 1
t = 1
while abs(t) > eps:
    if n < maks:
        n += 1
        t = ((-1)**(n - 1)) * (1 / (2 * n - 1))
        s += t
    else:
        break
if n + 1 > maks:
    print('За заданное число итераций \
не удалось вычислить сумму последовательности')
else:
    y = 4 * s
    print(('Сумма = ' + '{:7.6g}' +' Кол-во итераций = ' + '{}').format(y, n))
        
    
    
