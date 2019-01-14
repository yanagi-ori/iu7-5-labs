n = int(input('Введите размер матрицы: '))
m = n
A = []
for i in range(n):
    A.append([])
    for j in range(m):
        A[i].append(int(input('Введите элемент {}-й строки  + {}-ого столбца: '.format(i,j))))


for i in range(n):
    for j in range(n):
        print('{:3}'.format(A[i][j]), end = ' ')
    print()
print()
    

for i in range(n):
    for j in range(i):
        A[i][j], A[j][i] = A[j][i], A[i][j]



for i in range(n):
    for j in range(n):
        print('{:3}'.format(A[i][j]), end = ' ')
    print()
print()

for i in range(n):
    A[i][0], A[i][n - 1] = A[i][n - 1], A[i][0]
    

for i in range(n):
    for j in range(n):
        print('{:3}'.format(A[i][j]), end = ' ')
    print()

