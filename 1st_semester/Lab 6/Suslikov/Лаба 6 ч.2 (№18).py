#   Сусликов Д. ИУ7-15б
#   Лабараторная работа 6 (18) часть 2

#   N - размер массива, b - число, k - число макс. чисел,
#   maks - максимальное число, a,с - массивы, j,i - номера чисел в массиве

#   Ввод массива и числа
N = input('Введите размер массива ')
while N.replace('e','',1).isdigit() == False or N == '0':
    N =(input('Ошибка! Введите размер массива '))
N = float(N)
N = int(N)

a = [0] * N
for i in range(N):
    print('a['+str(i)+ '] = ', sep = '', end = '')
    a[i]=(input())
    a[i].strip()
    while a[i].lstrip('-').replace('.','',1).replace('e-','',1).replace('e','',1).isdigit() == False:
        a[i]=(input('Ошибка! Введите число массива ещё раз '))
    a[i] = float(a[i])
print(a)

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

#   Создание массива с числом после каждого макс.
j = 0
c = [0]*(len(a) + k)
for i in range (len(a)):
    c[j] = a[i]
    j += 1
    if a[i] == maks:
        c[j] = ('{:.5g}'.format(b))
        j+=1                                             
print(c)
