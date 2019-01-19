n = int(input('Введите кол-во элементов в массиве: '))
A = [0] * n
k = 0
for i in range(n):
    A[i] = int(input('Введите элемент: '))
    if A[i] % 2 == 0:
        k += A[i] % 10
q = 0
t = n
for i in range(n):
    if (i+1) % 3 == 0:
        A[i] = None
print(A)
p=len(A)
d = 0
y = 0
for i in range(n):
    if A[i] is not None:
        A[i], A[d] = A[d], A[i]
        d += 1
        p -= 1
    else:
        y += 1
p+=1
q=0
A+=[0]
i = len(A)-1
while t >= 0:
    if (i-q) >= 0:
        if (i-1) >= 0:
            if i != p:
                A[i-q] = A[i-1]
            else:
                A[i-q] = k
                q+=1
    t-=1
    i-=1
print(A)
for i in range(n-y+1):
    print(A[i], end=' ')