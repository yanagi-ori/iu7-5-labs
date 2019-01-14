#   A - матрица, sr(0-4) - средние значения 1-5 строк соответственно
#   srmaks - максимальное среднее значение, f - длина А

A = [[0,2,3,4,5],
     [1,0,6,7,8],
     [1,1,0,9,10],
     [1,1,1,0,11],
     [1,1,1,1,0]]

#   Вывод матрицы

for q in A:
    print(q)
print()

f = len(A)
for i in range(f):
    for j in range(f):
        print('{:3}'.format(A[i][j]), end = ' ')
    print()

sr = [0] * (i+1)

#   Подсчёт средних значений 
for j in range(f):
    for i in range(f):
        sr[i] += (A[i][j] / f)

#   Максимальное среднее значение

srmaks = max(sr)

#   Вывод
for i in range(len(sr)):
    print(('Среднее арифметическое строки № '+'{}'+' = '+'{:.2g}').format(i+1,sr[i]))
    
print()
print(('Наибольшее среднее арифметическое = '+'{:.2g}').format(srmaks))


    
