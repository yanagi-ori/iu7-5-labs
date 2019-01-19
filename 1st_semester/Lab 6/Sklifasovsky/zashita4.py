N = int(input('Введите кол-во чисел в массиве: '))
A = [0]*N
k = 0
p = 1
for i in range(N):
    A[i] = int(input('Введите число: '))
    if A[i] >= 0 and A[i] <= 10:
        k+=1
        p *= A[i]




srgeom = p/k
A+=[0]
N=len(A)
i = len(A)-1
q = N
while N != 0:
        if i != 0:
            A[i] = A[i-1]
        N-=1
        i-=1

for i in range(q):
    if A[i] > 0:
        A[i] = None

d = 0
for i in range(q):
    if A[i] is not None:
        if A[i] > 0:
            A[i], A[d] = A[d], A[i]
            d +=1

A[0] = srgeom





print(A)
