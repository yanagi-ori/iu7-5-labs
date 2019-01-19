from math import sqrt, pi, cos
#Вводим координаты
Ax = float(input('Введите координату x точки A: '))
Ay = float(input('Введите координату y точки A: '))
Bx = float(input('Введите координату x точки B: '))
By = float(input('Введите координату y точки B: '))
Cx = float(input('Введите координату x точки C: '))
Cy = float(input('Введите координату y точки C: '))


abx = float(Bx-Ax)    #Координата x вектора ab
aby = float(By-Ay)    #Координата y вектора ab
bcx = float(Cx-Bx)    #Координата x вектора bc
bcy = float(Cy-Bx)    #Координата y вектора bc
acx = float(Cx-Ax)    #Координата x вектора ac
acy = float(Cy-Ay)    #Координата y вектора ac

ab = float(sqrt((Bx-Ax)**2+(By-Ay)**2))
bc = float(sqrt((Cx-Bx)**2+(Cy-By)**2))
ac = float(sqrt((Cx-Ax)**2+(Cy-Ay)**2))





cosABAC = float((abx * acx + aby * acy) / ((sqrt(abx ** 2 + aby ** 2)) * (sqrt(acx ** 2 + acy ** 2))))  # угол между AB и AC
cosABBC = float((abx * bcx + aby * bcy) / ((sqrt(abx ** 2 + aby ** 2)) * (sqrt(bcx ** 2 + bcy ** 2))))  # угол между AB и BC
cosBCAC = float((bcx * acx + bcy * acy) / ((sqrt(bcx ** 2 + bcy ** 2)) * (sqrt(acx ** 2 + acy ** 2))))  # угол между BC и AC

cosmax = max(cosABAC, cosABBC, cosBCAC)  # Вычисляем максимальный косинус
p = (ab+bc+ac)/2
SABC = sqrt(p*(p-ab)*(p-bc)*(p-ac))
if cosmax == cosABAC:

    HCAB = float((2 * SABC) / ac)  # Нахождение высоты треугольника CAD
    print('Высота из наименьшего угла = {:.5}'.format(HCAB)) #Форматный вывод высоты
elif cosmax == cosABBC:
    HABC = float((2 * SABC) / ab)  # Нахождение высоты треугольника ABD
    print('Высота из наименьшего угла = {:.5}'.format(HABC)) #Форматный вывод высоты
elif cosmax == cosBCAC:
    HBCA = float((2 * SABC) / bc)  # Нахождение высоты треугольника BCD
    print('Высота из наименьшего угла = {:.5}'.format(HBCA)) #Форматный вид


