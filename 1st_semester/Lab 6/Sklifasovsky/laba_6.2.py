# Склифасовский Денис ИУ7-15
# Программа случайно сгенерируемый массив


import random


N = int(input('Введите количество чисел в массиве: '))
A, B = map(float, input('Введите интервал массива: ').split())
C = [0]*N
for i in range(N):
    C[i] = random.uniform(A,B)
    C[i] = round(C[i],5)
print(C)
