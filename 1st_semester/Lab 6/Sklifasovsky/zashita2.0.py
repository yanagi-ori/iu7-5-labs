#Склифасовский Денис ИУ-7 15
#Защита
N = int(input('Введите кол-во чисел в массиве: '))
A = [0]*N
n = A[0]
k = 0
k1 = 0
q = 0
for i in range(N):
    A[i] = float(input(''))
    if n > A[i]:
        n = A[i]
    if A[i] < 0:
        k += 1
        k1 += A[i]
for i in range(N):
    if A[i] == n:
        q += 1
p = 0
print(A)
if k == 0:
    print('Не найдено среднее арифметическое')
else:
    kc = k1/k
    print(kc)
    t = 0
'''   B = [0] * (N + q)
    for i in range(N):
        if A[i] != n:
            B[i+p] = A[i]
        else:
            B[i+p] = A[i]
            B[i+1+p] = kc
            p+=1
    print(B)'''
    for i in range(N):
            if A[i] == n:
                A += 0
                for l in range(N+1, i + 1, -1):
                    A[i-1]
            else:
                B[i+p] = A[i]
                B[i+1+p] = kc
                p+=1