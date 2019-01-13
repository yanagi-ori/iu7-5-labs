n = int(input('Введите размер матрицы (n*n): '))
a = [[0 for i in range(n)] for j in range(n)]
start_line = 0
x = start_line
for i in range(len(a)):
    for r in range(start_line, len(a)):
        a[r][i] = a[i][r] = x
        x += 1
    start_line += 1
    x = 0

for i in range(n):
    for j in range(n):
        print('{:^3g}'.format(a[i][j]), end='')
    print()
