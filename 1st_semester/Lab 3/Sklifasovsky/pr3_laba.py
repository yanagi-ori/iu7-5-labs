from math import sqrt, pi, cos

Ax = float(input('Введите координату x точки A: ')) #Координата x точки A
Ay = float(input('Введите координату y точки A: ')) #Координата y точки A
Bx = float(input('Введите координату x точки B: ')) #Координата x точки B
By = float(input('Введите координату y точки B: ')) #Координата y точки B
Cx = float(input('Введите координату x точки C: ')) #Координата x точки C
Cy = float(input('Введите координату y точки C: ')) #Координата y точки C

ab = float(sqrt((Bx-Ax)**2+(By-Ay)**2))    #Длина ab
bc = float(sqrt((Cx-Bx)**2+(Cy-By)**2))    #Длина bc
ac = float(sqrt((Cx-Ax)**2+(Cy-Ay)**2))    #Длина ac

abx = float(Bx-Ax)    #Координата x вектора ab
aby = float(By-Ay)    #Координата y вектора ab
bcx = float(Cx-Bx)    #Координата x вектора bc
bcy = float(Cy-Bx)    #Координата y вектора bc
acx = float(Cx-Ax)    #Координата x вектора ac
acy = float(Cy-Ay)    #Координата y вектора ac



A1x = float((Bx+Cx)/2)   # Координата x конца медианы AA1
A1y = float((By+Cy)/2)   # Координата y конца медианы AA1
B1x = float((Ax+Cx)/2)   # Координата x конца медианы BB1
B1y = float((Ay+Cy)/2)   # Координата y конца медианы BB1
C1x = float((Ax+By)/2)   # Координата x конца медианы CC1
C1y = float((Ay+By)/2)   # Координата y конца медианы CC1

if (ab+bc > ac) and (ab+ac > bc) and (bc+ac > ab):      #Проверяем существует ли данный треугольник
    AA1 = float(sqrt((A1x-Ax)**2+(A1y+Ay)**2))   #Длина медианы AA1
    BB1 = float(sqrt((B1x-Bx)**2+(B1y+By)**2))   #Длина медианы BB1
    CC1 = float(sqrt((C1x-Cx)**2+(C1y+Cy)**2))   #Длина медианы CC1

    cosABAC = float((abx*acx + aby*acy)/((sqrt(abx**2 + aby**2))*(sqrt(acx**2 + acy**2)))) #угол между AB и AC
    cosABBC = float((abx*bcx + aby*bcy)/((sqrt(abx**2 + aby**2))*(sqrt(bcx**2 + bcy**2)))) #угол между AB и BC
    cosBCAC = float((bcx*acx + bcy*acy)/((sqrt(bcx**2 + bcy**2))*(sqrt(acx**2 + acy**2)))) #угол между BC и AC

    cosABACR = float((cosABAC*180)/pi) #угол между AB и AC в градусах
    cosABBCR = float((cosABBC*180)/pi) #угол между AB и BC в градусах
    cosBCACR = float((cosBCAC*180)/pi) #угол между BC и AC в градусах

    cosmax = max(cosABACR,cosABBCR,cosBCACR) #Вычисляем максимальный косинус
    if cosmax == cosABACR:                   #Проверяем какой угол является максимальным
        print('Медиана = ', AA1)
    elif cosmax == cosABBCR:
        print('Медиана = ', BB1)
    elif cosmax == cosBCACR:
        print('Медиана = ', CC1)
    Dx = float(input('Введите координату X точки D: ')) #Вводим дополнительную координату X точки D
    Dy = float(input('Введите координату Y точки D: ')) #Вводим дополнительную координату Y точки D
    D1 = float((Ax - Dx)*(By - Ay) - (Bx - Ax)*(Ay - Dy))
    D2 = float((Bx - Dx)*(Cy - By) - (Cx - Bx)*(By - Dy))
    D3 = float((Cx - Dx)*(Ay - Cy) - (Ax - Cx)*(Cy - Dy))
    if (D1<=0 and D2<=0 and D3<=0) or (D1>=0 and D2>=0 and D3>=0):   #Проверяем принадлежит ли эта точка треугольнику

        ad = float(sqrt((Dx-Ax)**2 + (Dy-Ay)**2)) #нахождение длины стороны AD
        bd = float(sqrt((Dx-Bx)**2 + (Dy-By)**2)) #нахождение длины стороны BD
        cd = float(sqrt((Dx-Cx)**2 + (Dy-Cy)**2)) #нахождение длины стороны CD

        sinABD = float((ab**2 + bd**2 - ad**2)**2/((2*ab*bd)**2)) #Нахождение синуса угла ABD
        sinBCD = float((bc**2 + cd**2 - bd**2)**2/((2*bc*cd)**2)) #Нахождение синуса угла BCD
        sinCAD = float((ca**2 + ad**2 - cd**2)**2/((2*ab*ad)**2)) #Нахождение синуса угла CAD

        SABD = float(((ab*bd)/2)*sinABD) #Нахождение площади треугольника ABD
        SBCD = float(((bc*cd)/2)*sinBCD) #Нахождение площади треугольника BCD
        SCAD = float(((ac*ad)/2)*sinCAD) #Нахождение площади треугольника CAD

        HABD = float((2*SABD)/ab) #Нахождение высоты треугольника ABD
        HBCD = float((2*SBCD)/bc) #Нахождение высоты треугольника BCD
        HCAD = float((2*SCAD)/ac) #Нахождение высоты треугольника CAD

        maxH = max(HABD, HBCD, HCAD)          #Вычисление максимальной высоты среди треугольников ABD, BCD, CAD
        print('Расстояние от точки D до дальней стороны = ', maxH)  #Выводим расстояние на экран
        if (cosABAC == 0) or (cosBCAC == 0) or (cosBCAC == 0):      #Проверяем прямоугольный ли треугольник
            print('Треугольник является прямоугольным')
        if (cosABAC != 0) and (cosBCAC !=0) and (cosBCAC != 0):
            print('Треугольник не является прямоугольным')

else:
    print('Такого треугольника не существует')
