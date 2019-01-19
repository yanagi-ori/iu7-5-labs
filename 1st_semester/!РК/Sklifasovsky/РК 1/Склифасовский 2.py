N = int(input('Введите кол-во элементов: '))
X = []
NOM = []


for i in range(N):
    X.append(X[i])

p = 0
q = X[0]
m = X[0]
for i in range(N):
    if X[i] >= m:
        m = X[i]
    if q == X[i]:
        p += 1


for i in range(N):
    print(X[i], end=' ')
print()


t = 0
for i in range(N):
    if X[i] == m:
        NOM.append(i+1)
        X[i] = None
        t += 1


d = 0
y = 0
for i in range(N):
    if X[i] is not None:
        X[i], X[d] = X[d], X[i]
        d += 1
    else:
        y += 1


for i in range(t):
    print(NOM[i], end=' ')
print()

if p == N:
    print('Все элементы одинаковые')
else:
    for i in range(N-y):
        print(X[i], end=' ')

