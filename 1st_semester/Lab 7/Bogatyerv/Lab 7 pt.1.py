import random

A = [random.randrange(0, 10) for i in range(5)]
B = [random.randrange(0, 10) for j in range(6)]
C = []
SR = []
N = []
print('Исходные массивы:\n', A, B, '\n')
print('{:^18}'.format('Matrix'), '|', 'Average', '|', ' Over', sep='')
print('-'*32)
for i in range(5):
    armean = 0
    C.append([])
    for j in range(6):
        C[i].append(A[i]*B[j])
        armean += C[i][j]
    SR.append(armean/6)


for i in range(5):
    ova = 0
    for j in range(6):
        if SR[i] < C[i][j]:
            ova += 1
        print('{:^2}'.format(C[i][j]), end=' ')
    N.append(ova)
    print('|', '{:^7}'.format('{:.3g}'.format(SR[i])), '| ', N[i], sep='')
