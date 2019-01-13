#   Сусликов Д. ИУ7-15б
#   Лабараторная работа 6 (18) часть 2

#   N - размер массива, b - число, k - число макс. чисел,
#   maks - максимальное число, a,с - массивы, j,i - номера чисел в массиве

#   Ввод массива и числа c проверкой

N = input('Введите размер массива ')
while N.isdigit() == False or N == '0':
    N =(input('Ошибка! Введите размер массива '))
N = float(N)
N = int(N)

#   Заполнение массива с проверкой

a = [0] * N
for i in range(N):
    a[i]= input('Число в массиве = ')
    a[i].strip()
    while a[i].lstrip('-').replace('.','',1).replace('e-','',1).replace('e+','',1).replace('e','',1).isdigit() == False:
        a[i]=(input('Ошибка! Введите число массива ещё раз '))
    a[i] = float(a[i])
print(a)

#   Ввод числа с проверкой

b = input('Введите число ')
b.strip()
while b.lstrip('-').replace('.','',1).replace('e-','',1).replace('e','',1).isdigit() == False:    
    b = input('Введите число ')
b = float(b)

    
k = 0
maks = a[0]

#   Определение максимума и определение кол-ва максимальных чисел

for i in range (N):
    if a[i] >= maks:
        maks = a[i]
        k += 1

#   Проверка на лишнее

if a[0] < maks:
    k = k - 1

#   Увеличение массива

a = a + ([0]*k)


#   Вставка числа
if len(a) == 2:
    a[1] = b
else:
    for i in range(len(a)):
       if a[i] == maks:        
            u=i+1
            for i in range(len(a)-1,i,-1):
                a[i] = a[i-1]
            a[u] = b
        
print(a)
