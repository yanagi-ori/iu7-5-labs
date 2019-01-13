K = int(input('Введите размер матрицы (K * K): '))
A = [[0 for i in range(K)] for j in range(K)]
for i in range(K):
    A[i][K-i-1] = K+i
for j in range(K - 1):
        A[0][j] = j+1
for i in range(1, K):


for i in range(K):
    print(A[i])