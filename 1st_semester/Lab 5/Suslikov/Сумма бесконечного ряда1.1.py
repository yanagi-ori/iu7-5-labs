# Cусликов Д. ИУ7-15б
# Cумма бесконечного ряда

# n - номер итерации, y - сумма, x - вводимая переменная
# t - текущий член последовательности, maks - максимальное число итераций
# eps - точность, xh - шаг вывода в таблице, nt - № итерации в таблице


x = float(input('Введите  0 < x < 1 '))

# Проверка введенного х

while x >= 1 or x <= 0:
    print('Неверный ввод x! Попробуйте ещё раз.')
    x = float(input('Введите  0 < x < 1 '))
     
xh = float(input('Введите шаг '))
eps = float(input('Введите точность '))
maks = float(input('Введите максимальное число итераций '))

# Начальные данные

n = 1   
y = x   
t = x   
nt = 1 + xh

# Таблица

print('_' * 79)
print('|  № итерации   \
|  Текущий член |Значение суммы |')
print(('|{:^15}|{:^15g}|{:^15g}|').format(n, t, y))

# Цикл подсчёта

while abs(t) > eps:   # Проверка по точности
    if n < maks:      # Проверка того, что не зашли за максимум итераций

        # Подсчёт
        
        n = n + 1
        t = ((-1)**(n + 1)) * ((x**(2 * n - 1)) /(2 * n - 1))
        y = y + t

        # Вывод в таблицу с определённым шагом
        
        if nt == n:
            nt += xh
            print(('|{:^15}|{:^15g}|{:^15g}|').format(n, t, y))            

# Если итераций потребовалось больше максимума - остановка
        
    else:
        
        break
# Если итераций больше максимума - вывод сообщения об этом

if n + 1 > maks:
    print('-' * 79)
    print('За заданное число итераций \
не удалось вычислить сумму последовательности')

# Если итераций меньше максимума - вывод суммы и кол-ва итераций

else:
    print('-' * 79)
    print(('Сумма = ' + '{:7.6g}' +' Кол-во итераций = ' + '{}').format(y, n))


        

              
              
        
              
            
     
                 
     
                                                     
                                                     
        
      
    
    
