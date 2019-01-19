''' Эта программа на вход принимает значение ребра и выводит объем,
площадь боковой поверхности и радиусы вписанной и описанной сферпы Икосаэдра   '''

''' Склифасовский Денис  ИУ7-15Б'''

from math import log10,sqrt #Импортируем десятичный логарифм и корень из math

n = float(input('Введите размер ребра икосаэдра: '))


if n < 0:
    print('Введено отрицательное значение')
else:
    V = (5*(n**3)*(3 + sqrt(5)))/12      #Формула объема икосаэдра
    print('Ваш объем равен: ' + str("%.5g" % (V)))  #Форматный вывод объема


    S = 5*(n**2)*sqrt(3)  #Формула площади боковой поверхности икосаэдра
    print('Площадь поверхности равна: ' + str("%.5g" % (S)))  #Форматный вывод площади боковой поверхности

    r1 = (n*sqrt(3)*(3 + sqrt(5)))/12 #Формула радиуса вписанной сферы икосаэдра
    print('Радиус вписанной сферы равен: ' + str("%.5g" % (r1))) #Форматный вывод радиуса сферы икосаэдра

    r2 = (n*sqrt(2*(5 + sqrt(5))))/4 #Формула радиуса описанной сферы икосаэдра
    print('Радиус описанной сферы равен: ' + str("%.5g" % (r2))) #Форматный вывод радиуса описанной сферы
