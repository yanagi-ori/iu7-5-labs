# Программа вычисляет данный интеграл способом трапеций
# и левых прямоугольников на отрезке [a,b].
# Также, для наименее точного из этих двух методов производится вычисление интеграла
# с заданной точностью eps, высчитывается относительная и абсолютная ошибка.
# Жигалкин Дима. ИУ7-15Б
from math import exp
from sys import exit

def trapec(f, a, b, n):
    h = float(b - a)/n
    result = 0.5*(f(a) + f(b))
    for i in range(1, n):
	    result += f(a + i*h)
    result *= h
    return result
    
def triangle(f, a, b, n):
    total = 0
    h = float(b - a)/n
    for k in range(0, n):
        total += f(a + k*h)  
    result = h * total
    return result

def perv(g, a, b):
    Itoch = g(b)-g(a)
    return Itoch

try:
    eps = float(input('Введите точность: '))
    print('Ввод отрезка интегрирования')
    a, b = map(int, input('Задайте точку a отрезка [a,b]: ').split())
except ValueError:
    print('Try again')
    exit()
if a > b:
    print('Try again')
    exit()
f = lambda x: (x**4/12 + x/3 - 1/60)
g = lambda x: x**5/60 + x**2/6 - x/60

# Интегралы при заданных условием n.
I10 = trapec(f, a, b, 10)
I100 = trapec(f, a, b, 100)

V10 = triangle(f, a, b, 10)
V100 = triangle(f, a, b, 100)

s1='\u250C'   # Символы unicode, необходимые для рисования таблицы.
s2='\u2500'
s3='\u252C'
s4='\u2510'
s5='\u2502'
s6='\u251C'
s7='\u2534'
s8='\u2524'
s9='\u2514'
s10='\u2518'

# Вывод и заполнение таблицы.
print(s1+17*s2+s3+15*s2+s3+15*s2+s4)               
print(s5+'{:^8}'.format('Метод')+'         '+s5+'{:^15}'.format('n1 = 10')+s5+\
      '{:^15}'.format('n2 = 100')+s5)

print(s6+17*s2+s7+15*s2+s7+15*s2+s8)
    
print(s5,'{:^8}'.format('Трапеции'),'{:>20.7f}'.format(I10),\
      '{:>15.7f}'.format(I100)+'   '+s5)
print(s5,'{:^8}'.format('Левых прямоуг.'),'{:>14.7f}'.format(V10),\
      '{:>15.7f}'.format(V100)+'   '+s5)
print(s9+49*s2+s10)
# Считаем с заданной точностью.
n = 1
a1 = triangle(f, a, b, n)
n *= 2
a2 = triangle(f, a, b, n)

while abs(a1 - a2) > eps:
    n *= 2
    a1 = triangle(f, a, b, n)
    n *= 2
    a2 = triangle(f, a, b, n)
    
absolute_error = abs(perv(g, a, b) - a2)
otnos_error = (absolute_error * 100/perv(g, a, b))
print("Значение интеграла, вычисленное с заданной точностью eps: ", '{:>1.7f}'.format(a2),\
      "\nКоличество разбиений:", n)
print('Абсолютная ошибка: ', '{:>1.7f}'.format(absolute_error))
print('Относительная ошибка: ','{:>1.2f}'.format(otnos_error),'%')



