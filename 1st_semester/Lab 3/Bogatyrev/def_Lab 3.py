from math import sqrt, cos, acos

x1, y1 = map(float, input('Введите координаты первой точки: ').split())
x2, y2 = map(float, input('Введите координаты первой точки: ').split())
x3, y3 = map(float, input('Введите координаты первой точки: ').split())

AB = sqrt((x2 - x1)**2 + (y2 - y1)**2)
BC = sqrt((x3 - x2)**2 + (y3 - y2)**2)
AC = sqrt((x1 - x3)**2 + (y1 - y3)**2)

if (AC + AB) < BC or (AB + BC) < AC or (AC + BC) < AB \
            or (x1 == x2 and y1 == y2) or (x2 == x3 and y2 == y3) or (x1 == x3 and y1 == y3):
    print('Треугольник не существует')
else:
    if AB > BC:
        maxSideValue = AB
        angle = acos((AC ** 2 + BC ** 2 - AB ** 2) / (2 * AC * BC))
        bisector = (2 * BC * AC * cos(angle / 2)) / (BC + AC)
    else:
        maxSideValue = BC
        angle = acos(((AB ** 2 + AC ** 2 - BC ** 2) / (2 * AB * AC)))
        bisector = (2 * AB * AC * cos(angle / 2)) / (AB + AC)
    if maxSideValue < AC:
        angle = acos(((BC ** 2 + AB ** 2 - AC ** 2) / (2 * AB * BC)))
        bisector = (2 * AB * BC * cos(angle / 2)) / (AB + BC)

    print('Биссектриса из большего угла:', '{:.7g}'.format(bisector))