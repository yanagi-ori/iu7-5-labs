# Склифасовский Денис ИУ-7 15
# Программа вставляет в начало произведение чисел деленное на
# кол-во в диапозоне от 0 до 10
# И удаляет все положительные числа
N = int(input('Введите кол-во чисел в массиве: '))

k = 0
p = 1
A=[]
for i in range(N):
    t = int(input('Введите число: '))

    if t >= 0 and t <= 10:
        k += 1
        p *= t
    if t <= 0:
        A += [t]

srgeom = p/k
A+=[0]
N=len(A)
i = len(A)-1
while N != 0:
        if i != 0:
            A[i] = A[i-1]

        N-=1
        i-=1
A[0] = srgeom
i = len(A)-1
N = len(A)
for i in range(N):
    if A[i] > 0:
        A[i] = None

for i in range(N):
    print('{:5}'.format(A))
print(A)
