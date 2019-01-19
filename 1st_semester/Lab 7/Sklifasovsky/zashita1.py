import random
M, N = map(int, input('Введите размер: ').split())
F = [[0]*N for _ in range(M)]
A = [[1]*N for _ in range(M)]
t = int(input('Введите начало отрезка '))
n = int(input('Введите конец отрезка '))
for i in range(M):
    for j in range(N):
        F[i][j] = random.randint(t,n)
        #F[i][j] = float(input('Введите эелемент строки '))
        if F[i][j] == 0:
            A[i][j] = 0
for i in range(M):
    for j in range(N):
        print('{:^5}'.format(F[i][j]), end=' ')
    print()
print()
for i in range(M):
    for j in range(N):
        if A[i][j] == 0:
            for j in range(N):
                F[i][j] = 0




for i in range(M):
    for j in range(N):
        if A[i][j] == 0:
            for i in range(M):
                F[i][j] = 0

for i in range(M):
    for j in range(N):
        print('{:^5}'.format(F[i][j]), end=' ')
    print()

print()
for i in range(M):
    for j in range(N):
        print(A[i][j], end=' ')
    print()