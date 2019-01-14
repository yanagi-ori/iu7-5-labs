# 1 - интегрирование м-м левых прямоугольников
# 2 - интегрирование м-м парабол

# подключение библиотек
from math import sin, cos
from check import inptCrct as floatCrct, valueCompCrct as intCrct

# формирование функции
def y(x):
    return sin(x)
    
# строковые переменные
txtAB = ('Введите границы интегрирования - \n' + 
        'два действительных числа через пробел: ')
txtN = ('Введите участки разбиения для двух случаев - \n' +
        'два целых числа через пробел: ')
txtEPS = ('Введите требуемую точность - \n' +
         'положительное действительное число: ')
tableTop =  '┌' + '─'*20 + '┬' + '─'*20 + '┬' + '─'*20 + '┐'
tableMid =  '├' + '─'*20 + '┼' + '─'*20 + '┼' + '─'*20 + '┤'
tableBot =  '└' + '─'*20 + '┴' + '─'*20 + '┴' + '─'*20 + '┘' 
metod = '{:^20}'
metodArg =  '{:^6g}'
razb = '{:^20}'
razbArg =  'n{0} = {1}'
znach = '{:.10g}'

# входные данные
ab = input(txtAB)
n1n2 = input(txtN)
eps = input(txtEPS)

# проверка входных данных на корректность
if len(ab.split()) < 2 or len(n1n2.split()) < 2:
    print('Введены некорректные данные')
    exit()
if not (floatCrct(ab.split()[0])*floatCrct(ab.split()[1])*intCrct(n1n2.split()[0])\
    *intCrct(n1n2.split()[1])*floatCrct(eps)):
    exit()
a, b, eps = map(float,ab.split()+[eps])
n1, n2 = map(int,n1n2.split())


if (a >= b) or abs(eps) <= 10**(-1000) or eps < 0 or n1 < 0 or n2 < 0:
    exit()

# 1 - ф-ция интегр-ия м-м левых прямоугольников
def integrLeftRect(a,b,n):
    h = (b-a)/n
    s = 0
    for i in range(n):
        s += (y(a + h*i))
    return h*s

# 2 - ф-ция  интегр-ия м-м парабол
def integrParabol(a,b,n):
    h = (b-a)/(2*n)
    s2 = s4 = 0
    for i in range(1,n+1):
        s2 += y(a + 2*i*h)
        s4 += y(a + (2*i-1)*h)
    return (h/3)*(y(a) + y(b) + 2*s2 + 4*s4 - 2*y(a + 2*n*h))
        

# 3 - точное значение интеграла для функции
absIntegrVal = cos(a)-cos(b)

resLeftRect1 = integrLeftRect(a,b,n1)
resLeftRect2 = integrLeftRect(a,b,n2)
resParabol1 = integrParabol(a,b,n1)
resParabol2 = integrParabol(a,b,n2)

# Вывод результатов в таблицу:
print(tableTop)
print('│'+ metod.format('Метод/разбиение') + '│' + razb.format(razbArg.format(1, n1))
      + '│' + razb.format(razbArg.format(2, n2)) + '│')
print(tableMid)
print('│'+ metod.format('Левые прям-ки') + '│' + razb.format(znach.format(resLeftRect1))
      + '│' + razb.format(znach.format(resLeftRect2)) + '│')
print(tableMid)
print('│'+ metod.format('Параболы') + '│' + razb.format(znach.format(resParabol1))
      + '│' + razb.format(znach.format(resParabol2)) + '│')
print(tableBot)

print()

# Интегрирование до требуемой точности методом прямоугольников
n = 1
sOld = 0
sNew = integrLeftRect(a,b,n)
while abs(sOld - sNew) > eps:
    n *= 10
    sOld = sNew
    sNew = integrLeftRect(a,b,n)
    
# развернутый ответ
print('Точное значение интеграла функции:', '{:.10g}'.format(absIntegrVal))
print()
print('Абсолютная погрешность, м. левых прям-ков, разбиение = {}: '.format(n1), '{:.10g}'.format(abs(resLeftRect1 - absIntegrVal)))
print('Абсолютная погрешность, м. левых прям-ков, разбиение = {}: '.format(n2), '{:.10g}'.format(abs(resLeftRect2 - absIntegrVal)))
print('Абсолютная погрешность, м. парабол, разбиение = {}: '.format(n1), '{:.10g}'.format(abs(resParabol1 - absIntegrVal)))
print('Абсолютная погрешность, м. парабол, разбиение = {}: '.format(n2), '{:.10g}'.format(abs(resParabol2 - absIntegrVal)))
print()
print('Интеграл, вычисленный с указанной точностью м-м левых прям-ков: ', '{:.10g}'.format(sNew))
print('Абсолютная погрешность: ', '{:.10g}'.format(abs(absIntegrVal-sNew)))
if absIntegrVal != 0:
    print('Относительная погрешность: ', '{:.10g}'.format(abs(absIntegrVal-sNew)/absIntegrVal))
else:
    print('Невозможно вычислить относительную погрешность')


    

    
