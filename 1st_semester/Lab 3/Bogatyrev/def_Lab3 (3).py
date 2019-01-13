from math import sqrt

print('Введите значения координат точек вершин треугольника')
Ax, Ay = map(float, input('Введите координаты первой точки через пробел: ').split())
Bx, By = map(float, input('Введите координаты второй точки через пробел: ').split())
Cx, Cy = map(float, input('Введите координаты третьей точки через пробел: ').split())

if (Ax == Bx and Ay == By) or (Bx == Cx and By == Cy)\
        or (Ax == Cx and Ay == Cy):
    print('Недопустимые значения!')
else:
    print('~~~~~~~~~~~~~~~ Стороны треугольника ~~~~~~~~~~~~~~~') # Высчитать длины сторон
    AB = sqrt((Bx - Ax)**2 + (By - Ay)**2)
    BC = sqrt((Cx - Bx)**2 + (Cy - By)**2)
    AC = sqrt((Ax - Cx)**2 + (Ay - Cy)**2)
    print('AB =', '{:.7g}'.format(AB), '\nBC =', '{:.7g}'.format(BC),
          '\nAC =', '{:.7g}'.format(AC))
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

    anotherDotX, anotherDotY = \
        map(float, input('Введите координаты для еще одной точки:\nx = ').split())

    AM = sqrt((anotherDotX - Ax) ** 2 + (anotherDotY - Ay) ** 2)
    BM = sqrt((anotherDotX - Bx) ** 2 + (anotherDotY - By) ** 2)
    CM = sqrt((anotherDotX - Cx) ** 2 + (anotherDotY - Cy) ** 2)

    p1 = (BM + CM + BC) / 2
    p2 = (BM + AM + AB) / 2
    p3 = (AC + CM + AM) / 2

    h1 = 2 * sqrt(p1*(p1-BM)*(p1-CM)*(p1-BC)) / BC
    h2 = 2 * sqrt(p2*(p2-BM)*(p2-AM)*(p2-AB)) / AB
    h3 = 2 * sqrt(p3*(p3-AC)*(p3-CM)*(p3-AM)) / AC

    if round((anotherDotX - Ax)*(By - Ay) - (Bx - Ax)*(anotherDotY - Ay), 10) == 0 \
            or round((anotherDotX - Ax)*(Cy - Ay) - (Cx - Ax)*(anotherDotY - Ay), 10) == 0 \
            or round((anotherDotX - Ax) * (Cy - Ay) - (Cx - Ax) * (anotherDotY - Ay), 10) == 0:
        print('Точка находится на стороне треугольника')

    else:
        print('Расстояние от точки до ближайшей стороны', '{:.7g}'.format(min(h1, h2, h3)))
