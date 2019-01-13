from math import sqrt

x1, y1 = map(float, input("Введите координаты 1-й точки ").split())
x2, y2 = map(float, input("Введите координаты 2-й точки ").split())
x3, y3 = map(float, input("Введите координаты 3-й точки ").split())

#   Вычисление координат векторов
ax = x2 - x1
ay = y2 - y1
bx = x3 - x2
by = y3 - y2
cx = x1 - x3
cy = y1 - y3

#   Вычисление длин сторон треугольника
a = sqrt(ax**2 + ay**2)
b = sqrt(bx**2 + by**2)
c = sqrt(cx**2 + cy**2)
if (a + b > c) and (b + c > a) and (a + c > b):

    x4, y4 = map(float, input("Введите координаты 4-й точки ").split())

    #   Нахождение расстояния через площади малых треугольников

    #   Нахождение малых сторон
    d = sqrt((x1 - x4)**2 + (y1 - y4)**2)
    e = sqrt((x2 - x4)**2 + (y2 - y4)**2)
    f = sqrt((x3 - x4)**2 + (y3 - y4)**2)

    #   Полумериметр
    p1 = (a + d + e) / 2
    p2 = (e + b + f) / 2
    p3 = (f + c + d) / 2

    #   Площади
    s1 = sqrt(p1 * (p1 - a) * (p1 - d) * (p1 - e))
    s2 = sqrt(p2 * (p2 - e) * (p2 - b) * (p2 - f))
    s3 = sqrt(p3 * (p3 - f) * (p3 - c) * (p3 - d))

    # Расстояния
    h1 = (2 * s1) / a
    h2 = (2 * s2) / b
    h3 = (2 * s3) / c
    h = min(h1, h2, h3)
    print("Расстояние от точки до ближайшей стороны = "+'{:.5g}'.format(h))
else:
    print("Треугольник не существует")
