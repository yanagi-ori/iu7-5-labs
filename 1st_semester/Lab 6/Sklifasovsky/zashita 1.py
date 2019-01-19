N = int(input('Введите кол-во чисел в массиве: '))
A = [0]*N
n = A[1]
k = 0
k1 = 0
for i in range(N):
    A[i] = float(input(''))
    if n > A[i]:
        n = A[i]
    if A[i] < 0:
        k += 1
        k1 += A[i]
if k == 0:
    print('Не найдено среднее арифметическое')
else:
    kc = k1/k
    n = 0
    print(kc)
    for i in range(N):
        if k1 == A[i]:
            A+=[0]
            n+=1
    p = 0
    for i in range(N,k,-1):
        if i-n-p>=0:
            if A[i-n] != k1:
                A[i] = A[i-n]
            else:
                A[i-p] = kc
                A[i-1-p] = A[i-n-p+1]
                p+=1

    print(A)