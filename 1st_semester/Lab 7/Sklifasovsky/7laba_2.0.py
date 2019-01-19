from math import log
M = 12
N = 10
F = [[0]*N for _ in range(M)]
#ввод Z
z = [0]*10
for k in range(10):
    z[k] = input('Введите число: ')
    z[k].strip()
    while z[k].lstrip('-').replace('.','',1).replace('e-','',1).replace('e+','',1).replace('e','',1).isdigit() == False:
        z[k] = input('Ошибка, введите число еще раз: ')
    z[k] = float(z[k])

max_i = min_i = 0
min_sum = round(z[0] * log(0.1))
max_sum = round(z[0] * log(0.1))

for m in range(M):
    summ = 0

    for k in range(N):
        F[m][k] = round(z[k] * log(0.1+0.05*m), 5)
        summ += F[m][k]
        summ2 = summ
        #print(summ)
        if summ < min_sum:
            min_sum = summ
            min_i = m
        if summ > max_sum:
            max_sum = summ
            max_i = m
        #print('maxi - ',max_i, 'mini - ',min_i )

for i in range(12):
    for j in range(10):
        print('{:13}'.format(F[i][j]),end=' ')
    print()


W = F[max_i] + F[min_i]
for el in W:
    print(el)
