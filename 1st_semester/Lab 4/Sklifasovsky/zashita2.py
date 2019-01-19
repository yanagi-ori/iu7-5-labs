import math as m

def function(x):
    return x**2 - 36

xbeg, xend, h = map(float, input('Введите x первое, x конечное и шаг: ').split())

eps = int(-m.log10(h)+2)

y_min = y_max = function(xbeg)

x = xbeg

while x < xend:
    y = function(x)
    y_min = min(y, y_min)
    y_max = max(y, y_max)
    x = round(x + h, eps)

k = 70 / (y_max - y_min)

print('y min = ',y_min,'y max = ',y_max)

x = xbeg
if (y_max > 0 and y_min > 0) or (y_max < 0 and y_min < 0):
    while x <= xend:
        y = function(x)
        n = round((y - y_min) * k) + 1
        print('{:6} {:}*'.format(x, ' ' * n))

        x = round(x + h, eps)
else:
    index_OX = round(- y_min*k) + 1
    while x <= xend:
        y = function(x)
        str_x = '{:7} '.format(x)

        n = round((y - y_min) * k) + 1

        if y > 0:
            str_answer = ' ' * index_OX + '|' + ' '*(n - index_OX) + '*'
        elif y < 0:
            str_answer = ' '*(n-1) + '*' + ' '*(index_OX - n) + '|'
        else:
            str_answer = ' '*n + '*'
        print(str_x + str_answer)

        x = round(x + h, eps)
