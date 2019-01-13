# Защита 3 лабораторной работы
# Богатырев иван

from math import sqrt
from sys import exit


Ax, Ay = map(float, input('Введите координаты первой точки через пробел: ').split())
Bx, By = map(float, input('Введите координаты второй точки через пробел: ').split())
Cx, Cy = map(float, input('Введите координаты третьей точки через пробел: ').split())


AB = sqrt((Bx - Ax)**2 + (By - Ay)**2)
BC = sqrt((Cx - Bx)**2 + (Cy - By)**2)
AC = sqrt((Ax - Cx)**2 + (Ay - Cy)**2)


if (Ax == Bx and Ay == By) or (Bx == Cx and By == Cy) or (Ax == Cx and Ay == Cy)\
        or (AC + AB) < BC or (AB + BC) < AC or (AC + BC) < AB:
    exit('Недопустимые значения!')


p = (AB+AC+BC) / 2
S = round(sqrt(p * (p - AB)*(p - BC)*(p - AC)), 10)

cathetus1 = min(AB, AC, BC)
cathetus2 = (AB+AC+BC - cathetus1 - max(AB, AC, BC))


if round((cathetus1 * cathetus2 / 2), 10) == S:
    print('Треугольник прямоугольный')
else:
    print('Треугольник НЕ прямоугольный')