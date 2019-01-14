# xn- x нач. , xk - х конечный, xh - шаг, s - пробел
# ymin - у минимум, ymax - у максимум
# u - кол-во пробелов для оси у, z - кол-во пробелов для точки, 

from math import exp

xn = float(input('Введите х начальчный '))
xk = float(input('Введите х конечный '))
xh = float(input('Введите шаг '))
s = ' '
x = xn
y = x**2 - 25
ymin = y
ymax = y

while x < xk + xh / 2:
    y = x**2 - 25
    if -1e-10<= x < 1e-16:
        x = 0
    ymin = min(y, ymin)
    ymax = max(y, ymax)
    x+=xk

x = xn
u = int((0 - ymin) / (ymax - ymin) * 70)   #ось
round(u)
print(('{:12.5g}' + s * 55 + '{:12.5g}').format(ymin, ymax))
print('-' * 79 + '>')
while x < xk + xh / 2:
    y = x**2 - 25
    z = int((y - ymin) / (ymax - ymin) * 70) 
    round(z)

     # точки до оси
    if u != z and u > z:
        if -1e-10 <= x < 1e-16:
            x = 0
        print('{:7.6g}|'. format(x), s * z + '*' + s * (u - z - 1) + '|')

     #точки на оси
    elif u != z and u < z:
        if -1e-10 <= x < 1e-16:
            x = 0
        print('{:7.6g}|'. format(x), s * u + '|' + s * (z - u - 1) + '*')

    else:
        if -1e-10 <= x < 1e-16:
            x = 0
        print('{:7.6g}|'. format(x), s * z + '*')
    x += xh
print(s * (u + 8), 'V')
        

        
