#x1, y1 -координаты 1-й точки    
#x2, y2 -координаты 2-й точки    
#x3, y3 -координаты 3-й точки    
#x4, y4 -координаты 4-й точки

#xa, ya - координаты вектора а
#xb, yb - координаты вектора b
#xc, yc - координаты вектора с

#a - длина 1-й стороны, b - длина 2-й стороны, с - длина 3-й стороны

#uglA - градусная мера угла А, uglB - градусная мера угла B
#uglC - градусная мера угла С

#m - наибольший угол, med - медиана

#at, bt, ct - условия для принадлежности точки треугольнику

#d, e, f - длины отрезков от точки 4 до вершин треугольника
#p1, p2, p3 - полупериметры маленьких треугольников внутри основного
#s1, s2, s3 - площади маленьких треугольников внутри основного
#h1, h2, h3 - расстояния от точки 4 до сторон a, b, c - соответственно
#mh - наименьшее расстояние от точки 4 до одной из сторон треугольника



from math import sqrt, acos, degrees
x1, y1 = map(float, input("Введите координаты 1-й точки через пробел ").split())
x2, y2 = map(float, input("Введите координаты 2-й точки через пробел ").split())
x3, y3 = map(float, input("Введите координаты 3-й точки через пробел ").split())
xa = (x2 - x1)   # Вычисление координат векторов
ya = (y2 - y1)      
xb = (x3 - x2)
yb = (y3 - y2)
xc = (x1 - x3)
yc = (y1 - y3)

a = sqrt(xa**2 + ya**2)   # Вычисление длин сторон
b = sqrt(xb**2 + yb**2)
c = sqrt(xc**2 + yc**2)

if a + b > c and b + c>a and c + a > b:   # Условие существования треугольника
    print("1-ая сторона = " + '{:.5g}'.format(a))
    print("2-ая сторона = " + '{:.5g}'.format(b))
    print("3-ая сторона = " + '{:.5g}'.format(c))
    #Нахождение углов
    uglA = degrees (acos((a**2 + c**2 - b**2) / (2 * a * c)))  
    uglB = degrees (acos((a**2 + b**2 - c**2) / (2 * a * b)))
    uglC = degrees (acos((b**2 + c**2 - a**2) / (2 * b * c))) 
    m = max(uglA, uglB, uglC)    # Нахождение наибольшего угла
   
    # Вычисление медианы от наибольшего угла
    if m == uglA:
        med = (1 / 2) * sqrt(2 * a**2 + 2 * c**2 - b**2)    

    if m == uglB:
        med = (1 / 2 ) * sqrt(2 * a**2 + 2 * b**2 - c**2)

    if m == uglC:
        med = (1 / 2) * sqrt(2 * b**2 + 2 * c**2 - a**2)

    print("Медиана = "+'{:.5g}'.format(med))

    x4, y4 = map(float, input("Введите координаты 4-й точки ").split())

    # Условия для принадлежности точки треугольнику
    at = (x1 - x4) * (y2 - y1) - (x2 - x1) * (y1 - y4)
    bt = (x2 - x4) * (y3 - y2) - (x3 - x2) * (y2 - y4)   
    ct = (x3 - x4) * (y1 - y3) - (x1 - x3) * (y3 - y4)
    if (at >= 0 and bt >= 0 and ct >= 0) or (at <=0 and bt <=0 and ct <=0):
        print("Точка принадлежит треугольнику")

        # Нахождение расстояния (высоты) до ближайшей стороны при помощи площади  
        d = sqrt((x1 - x4)**2 + (y1 - y4)**2)
        e = sqrt((x2 - x4)**2 + (y2 - y4)**2)
        f = sqrt((x3 - x4)**2 + (y3 - y4)**2)
        p1 = ((a + d + e) / 2)
        p2 = ((e + b + f) / 2)
        p3 = ((d + f + c) / 2)
        s1 = sqrt(p1 * (p1 - a) * (p1 - d) * (p1 - e))
        s2 = sqrt(p2 * (p2 - e) * (p2 - b) * (p2 - f))
        s3 = sqrt(p3 * (p3 - d) * (p3 - f) * (p3 - c))
        h1 = (2 * s1) / a
        h2 = (2 * s2) / b
        h3 = (2 * s3) / c
        mh = min(h1, h2, h3)
        print("Наименьшее расстояние от точки до стороны "+'{:.5g}'.format(mh))
    else:
        print("Точка не принадлежит треугольнику")

    

    # Проверка на остроугольность треугольника
    if (uglA < 89.99999999999999) and (uglB < 89.99999999999999) and (uglC < 89.99999999999999):   
        print("Треугольник - остроугольный")
    else:
        print("Треугольник - не остроугольный")
else:
    print("Треугольник не существует")
    
    
