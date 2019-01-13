eps = float(input('input precision: '))
x = float(input('input number x: '))
n = 0; t = 1; y = 1
while abs(t) > eps:
    n += 1
    t *= x/n
    y += t
print('x =', x, '   y =', y)