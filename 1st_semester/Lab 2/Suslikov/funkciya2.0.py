x1 = float(input("Введите х1 "))
x2 = float(input("Введите х2 "))

# Первая вариация
if 0 <= x1 < 1:
    Y1 = -1
else:
    Y1 = 0
if -1 > x1:
    Y1 = 1
if -1 <= x1 < 0:
    Y1 = 0
print("x1=",x1," y1=",Y1)

# Вторая вариация 

if -1 > x2:
    Y2 = 1
if 0 <= x2 < 1:
    Y2 = -1
if (x2 >= 1) or (-1 <= x2 < 0):
    Y2 = 0
print("x2=", x2 ," y2=", Y2)


