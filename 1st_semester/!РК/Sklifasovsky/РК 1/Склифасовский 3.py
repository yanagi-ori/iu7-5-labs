N = int(input('Введите кол-во строк и столбцов: '))
X = [[0]*N for i in range(N)]
p = 5
for i in range(N):
    for j in range(N):
        t = 1
        for q in range(5):
            X[0][q] = t
            t += 1
        if i+j == 4:
            X[i][j] = p
            p+=1

for i in range(N):
    for j in range(N):
        if i == 3 and j == 0:
            X[i][j] = p
            p += 1
        if i == 2 and j == 0:
            X[i][j] = p
            p += 1
        if i == 1 and j == 0:
            X[i][j] = p
            p += 1


for i in range(N):
    for j in range(N):
        if i+j > 4:
            X[i][j] = 0




for i in range(N):
    for j in range(N):
        print('{:^5}'.format(X[i][j]), end=' ')
    print()