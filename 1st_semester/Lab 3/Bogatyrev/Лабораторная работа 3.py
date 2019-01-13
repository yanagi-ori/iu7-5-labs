# Лабораторная работа 3. Треугольник
# Вычисление необходимых данных по заданным координатам точек
# Богатырев Иван
#
# Ax, Ay, Bx, By, Cx, Cy - координаты точек вершин треугольника
# AB, BC, AC - стороны
# angleA, angleB, angleC - значения углов треугольника
# maxAngle - наибольший угол, maxAngleValue - его значение
# bisector - биссектриса наибольшего угла
# anotherDotX, anotherDotY - координаты четвертой точки (М)
# AM, BM, CM - отрезки, соединяющие т.М с вершинами треугольника
# dotInside - boolean, определяющ. положение т.М относительно треугольника
# mainS, s1, s2, s3 - площади основного треугольника и трех внутри соответственно
# h1, h2, h3 - высоты трех малых треугольников соответственно
# max_h - наибольшая высота из трех выше
# angleAMB, angleBMC, angleAMC - углы между прямыми AM, BM, CM


from math import sqrt, sin, cos, acos, degrees

print('Введите значения координат точек вершин треугольника:')
Ax, Ay = float(input('Для вершины A:\nx = ')), float(input('y = '))
Bx, By = float(input('Для вершины B:\nx = ')), float(input('y = '))
Cx, Cy = float(input('Для вершины C:\nx = ')), float(input('y = '))
if (Ax == Bx and Ay == By) or (Bx == Cx and By == Cy) \
        or (Ax == Cx and Ay == Cy):
    print('Недопустимые значения!')
else:
    print('~~~~~~~~~~~~~~~ Стороны треугольника ~~~~~~~~~~~~~~~')
    # Высчитать длины сторон
    AB = sqrt((Bx - Ax) ** 2 + (By - Ay) ** 2)
    BC = sqrt((Cx - Bx) ** 2 + (Cy - By) ** 2)
    AC = sqrt((Ax - Cx) ** 2 + (Ay - Cy) ** 2)
    print('AB =', '{:.7g}'.format(AB), '\nBC =', '{:.7g}'.format(BC),
          '\nAC =', '{:.7g}'.format(AC))
    if AB > BC:
        maxAngleValue = acos((AC ** 2 + BC ** 2 - AB ** 2) / (2 * AC * BC))
        bisector = (2 * BC * AC * cos(maxAngleValue / 2)) / (BC + AC)
    else:
        maxAngleValue = acos((AB ** 2 + AC ** 2 - BC ** 2) / (2 * AB * AC))
        bisector = (2 * AB * AC * cos(maxAngleValue / 2)) / (AB + AC)
    if maxAngleValue < AC:
        maxAngleValue = acos((BC ** 2 + AB ** 2 - AC ** 2) / (2 * AB * BC))
        bisector = (2 * AB * BC * cos(maxAngleValue / 2)) / (AB + BC)
    print('Биссектриса:', '{:.7g}'.format(bisector))
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

    anotherDotX, anotherDotY = \
        float(input('Введите координаты для еще одной точки:\nx = ')), \
        float(input('y = '))
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    p = AB + BC + AC
    mainS = sqrt(p * (p - AB) * (p - BC) * (p - AC))  # Нахождение площади основного треугольника

    # Вычисление расстояния от вершин треугольника до новой точки
    AM = sqrt((anotherDotX - Ax) ** 2 + (anotherDotY - Ay) ** 2)
    BM = sqrt((anotherDotX - Bx) ** 2 + (anotherDotY - By) ** 2)
    CM = sqrt((anotherDotX - Cx) ** 2 + (anotherDotY - Cy) ** 2)

    if (anotherDotX == Ax and anotherDotY == Ay) or \
            (anotherDotX == Bx and anotherDotY == By) \
            or (anotherDotX == Cx and anotherDotY == Cy):
        if anotherDotX == Ax:
            side = BC
        if anotherDotX == Bx:
            side = AC
        if anotherDotX == Cx:
            side = AB
        dotInside, trianglePart = True, True
        print('Точка находится внутри треугольника')

    else:
        trianglePart = False
        # Нахождение углов при вершине M
        angleAMB = acos((AM ** 2 + BM ** 2 - AB ** 2) / (2 * AM * BM))
        angleBMC = acos((BM ** 2 + CM ** 2 - BC ** 2) / (2 * BM * CM))
        angleAMC = acos((AM ** 2 + CM ** 2 - AC ** 2) / (2 * AM * CM))
        # Площади малых треугольников с вершиной M
        s1 = 0.5 * AM * BM * sin(angleAMB)  # основание AB
        s2 = 0.5 * BM * CM * sin(angleBMC)  # основание BC
        s3 = 0.5 * AM * CM * sin(angleAMC)  # основание AC
        # Сравнение площадей для определения, находится ли она внутри
        if round(s1 + s2 + s3, 10) == round(mainS, 10):  # abs(s1+s2+s3-mainS)<1e-10
            dotInside = True  # Внутри
            print('Точка находится внутри треугольника')
        else:
            dotInside = False  # Снаружи
            print('Точка не находится внутри треугольника')

    # Если точка внутри, находит высоту до самой удаленной стороны
    if dotInside:
        if trianglePart is False:
            h1 = 2 * s1 / AB
            h2 = 2 * s2 / BC
            h3 = 2 * s3 / AC
            if h1 > h2:
                max_h = h1
            else:
                max_h = h2
            if max_h < h3:
                max_h = h3
        else:
            max_h = 2 * mainS / side
        print('Расстояние до наиболее удаленной стороны:',
              "{:.7g}".format(max_h))

    # определение тупости треуглольника
    if round(degrees(maxAngleValue), 100) > 90:
        print('Треугольник тупоугольный')
    else:
        print('Треугольник не тупоугольный')
