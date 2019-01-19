#Программа, которая выводит таблицу значений 2 функций и выводит график первой
from math import sqrt, pi, cos, log, sin
#Ввод точки начала и конца
x1 = float(input("Точка начала промежутка: "))
x2 = float(input("Точка конца промежутка: "))
step = float(input("Шаг: "))

#Проверяем правильность ввода
if x1 > x2:
    x1, x2 = x2, x1




y = sin(x1) - 1
t = x1
ymin = y
ymax = y
a = 'Не определено'
#Цикл, который выводит значения
while x1 < (x2 + step/2):
    y = sin(x1) - 1
    ymin = min(y,ymin)
    ymax = max(y,ymax)
    x1 += step


x1 = t


print('Минимальное и максимальное значение равно: ' + str(ymin) + ', ' + str(ymax))
print('-'*80)
#Цикл, который выводит график
while x1 < (x2 + step/2):
    y = sin(x) - 1
    n = int((y - ymin) / (ymax - ymin) * 70)
    round(n)
    q = int((- ymin) / (ymax - ymin) * 70)
    round(q)
    print('{:<7.2}'.format(x1), end='')

    for i in range(71):
        if i == n:
            print('*', end='')
        elif i == q:
            print('|', end='')
        else:
            print(' ', end='')
    print()
    x1 += step



print(' ' *(q+6) + 'v')