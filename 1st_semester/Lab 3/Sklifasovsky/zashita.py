Ax = float(input('Введите координату x точки A: '))
Ay = float(input('Введите координату y точки A: '))
Bx = float(input('Введите координату x точки B: '))
By = float(input('Введите координату y точки B: '))
Cx = float(input('Введите координату x точки C: '))
Cy = float(input('Введите координату y точки C: '))

ab = (Bx-Ax)**2+(By-Ay)**2   #Длина ab
bc = (Cx-Bx)**2+(Cy-By)**2   #Длина bc
ac = (Cx-Ax)**2+(Cy-Ay)**2   #Длина ac


if ab == bc + ac or bc == ab + ac or ac == bc + ab:
    print('Треугольник прямоугольный')
else:
    print('Треугольник не является прямоугольным')