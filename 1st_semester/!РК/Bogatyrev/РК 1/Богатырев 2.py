from random import randrange

R = [randrange(0, 10) for i in range(int(input('Введите длину массива R (не больше 10): ')))]
print('Исходный массив R: ', end='')
for i in R:
    print(i, end=' ')
r_max = R[0]
NUM = []
for i in range(len(R)):
    if R[i] > r_max:
        r_max = R[i]
        NUM = [i + 1]
    elif R[i] == r_max:
        NUM += [i + 1]
print('\nПолученный массив NUM: ', end='')
for i in NUM:
    print(i, end=' ')
if len(R) == len(NUM):
    print('\nВсе элементы одинаковые')
else:
    for i in range(len(NUM)):
        del R[NUM[i - 1] - 1]
print('\nСжатый массив R: ', end='')
for i in R:
    print(i, end=' ')
