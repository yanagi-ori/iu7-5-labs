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
    x = float(x)
    return a

# Функция

def func(x):
    return cos(x)


# Интеграл через первообразную

def pobr(x,y):
    c = sin(x) - cos(y)
    return c

# Метод правых прямоугольников (без точности)
def integral(x,y,n):
    I = 0
    h = (y - x) / n
    for i in range(n):
        c = x + h
        I += func(c)
    I *= h
    return I
# Метод правых прямоугольников (c точностью до eps)

def integral2(x, y, n):
    I = 0
    h = (y - x) / n
    for i in range(n):
        if abs(integral(a, b, 2 * n) - integral(a, b, n)) < eps: 
            c = a + h
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
n1 = int(n1)
n2 = input('Введите второе кол-во участков: ')
n2 = proverkan(n2)
n2 = int(n2)
eps = input('Введите точность: ')
eps = proverka(eps)

# Интегралы

integr1 = integral2(a, b, n1) 
integr2 = integral2(a, b, n2)
integr3 = integral3(a, b, n1)
integr4 = integral3(a, b, n2)

# Таблица
print(64* '-')
print('|            Методы            | n1 = {:^8} | n2 = {:^8} |'.format(n1, n2))
print('| Метод правых прямоугольников |{:15.9g}|{:15.9g}|'.format(integr1, integr2))
print('| Метод трех восьмых           |{:15.9g}|{:15.9g}|'.format(integr1, integr2))
print(64* '-')

# Абсолютная и относительная точность

absolut = abs(pobr(a, b) - integr1)
otnosit = abs((pobr(a, b) - integr1) / pobr(a, b))

print ('Абсолютная точность = {:8g}'.format(absolut))
print ('Относительная точность = {:8g}'.format(otnosit))


