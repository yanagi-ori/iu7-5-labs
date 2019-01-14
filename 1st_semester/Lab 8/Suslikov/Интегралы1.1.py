from math import cos, sin

# Проверки

def proverka(x):
    x.strip()
    while x.lstrip('-').replace('.','',1).replace('e-','',1).replace('e+','',1).replace('e','',1).isdigit() == False: 
        x =(input('Ошибка! Введите число ещё раз '))
    x = float(x)
    return x

def proverkan(x):
    x.strip()
    while x.isdigit() == False or x == 0: 
        x =(input('Ошибка! Введите число ещё раз '))
    x = int(float(x))
    return x

# Функция

def func(x):
    return x**2


# Интеграл через первообразную

def pobr(x,y):
    c = 1/3 * y**3 - 1/3 * x**3
    return c


# Метод правых прямоугольников (без точности)

def integral(x,y,n):
    I = 0
    h = (y - x) / n
    for i in range(n):
        c = x + i * h
        I += func(c) * h
    I *= h
    return I


# Метод правых прямоугольников (c точностью до eps)

def integral2(x, y, n):
    I = 0
    h = (y - x) / n
    for i in range(n):
        if abs(integral(a, b, 2 * n) - integral(a, b, n)) > eps: 
            c = a + h * i
            I += func(c)
    I *= h
    return I


# Метод трех восьмых

def integral3(x, y, n):
    m = 3 * n - 1
    h = (y - x) / (3 * n)
    I = func(x) + func(y)
    for i in range(1, m):
        t = a + h * i
        if i % 3 == 0:
            I += 2 * func(t)
        else:
            I += 3 * func(t)
    I = I * 3 * h / 8
    return I
        
# Ввод с проверками

a = input('Введите нач. значение: ')
a = proverka(a)
b = input('Введите кон. значение: ')
b = proverka(b)
n1 = input('Введите первое кол-во участков: ')
n1 = proverkan(n1)
n2 = input('Введите второе кол-во участков: ')
n2 = proverkan(n2)
eps = input('Введите точность: ')
eps = proverka(eps)

# Интегралы

in1 = integral2(a, b, n1)

in3 = integral2(a, b, n2)

if n1 % 3 == 0:    
    in2 = integral3(a, b, n1)
else:
    in2 = 0

if n2 % 3 == 0:
    in4 = integral3(a, b, n2)
else:
    in4 = 0

# Таблица

print(64* '-')
print('|            Методы            | n1 = {:^8} | n2 = {:^8} |'.format(n1, n2))
print('| Метод правых прямоугольников |{:15.9g}|{:15.9g}|'.format(in1, in3))
print('| Метод трех восьмых           |{:15.9g}|{:15.9g}|'.format(in2, in4))
print(64* '-')

# Вывод при невозможноти подсчёта методом трех восьмых
if in2 == 0:
    print('Не удалось вычислить методом трех восьмых на {} отрезках - число отрезков не кратно 3'.format(n1))

if in4 == 0:
    print('Не удалось вычислить методом трех восьмых на {} отрезках - число отрезков не кратно 3'.format(n2))

# Абсолютная и относительная точности

absolut = abs(pobr(a, b) - in1)
otnosit = abs((pobr(a, b) - in1) / pobr(a, b))

print ('Абсолютная точность = {:8g}'.format(absolut))
print ('Относительная точность = {:8g}'.format(otnosit))


