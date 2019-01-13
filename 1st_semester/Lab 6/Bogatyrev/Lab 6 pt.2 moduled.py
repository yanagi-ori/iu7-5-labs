# Богатырев Иван
# Массивы. Вторая задача


from sys import exit

from iu7_basemodule import start_check

baka = False
check = ''
final = []
n = input('Задача №2\nВведите размер массива: ')
n_t = start_check(n, baka)
n = str(int(float(n)))

if (n.isdigit() or n_t.isdigit()) and int(n) >= 0:
    print('Введите значения массива (по одному):')
    n = int(float(n))
    orig_m = [0]*n
    for i in range(n):
        temp = input()
        orig_m[i] = temp
        start_check(temp, baka)
else:
    print('Wrong value was entered!')
    exit()


count = pos = neg = posNum_m_len = negNum_m_len = new_m_len = 0

# формирование длины списков отрицательных и положительных чисел
for i in range(len(orig_m)):
    if float(orig_m[i]) > 0:
        posNum_m_len += 1
        new_m_len += 1
    if float(orig_m[i]) < 0:
        negNum_m_len += 1
        new_m_len += 1

posNum_m = [0]*posNum_m_len
negNum_m = [0]*negNum_m_len

# наполнение списков положительных и отрицательных чисел
for i in range(len(orig_m)):
    if float(orig_m[i]) > 0:
        posNum_m[pos] = orig_m[i]
        pos += 1
    if float(orig_m[i]) < 0:
        negNum_m[neg] = orig_m[i]
        neg += 1

negNum_m.reverse()
neg_c = pos_c = 0

if len(posNum_m) <= 0:
    for i in range(neg):
        print(negNum_m[i])
elif len(negNum_m) <= 0:
    for i in range(pos):
        print(posNum_m[i])
else:
    for i in range(0, (pos + neg)):
        if i % 2 == 0:
            if pos_c < pos:
                print(posNum_m[pos_c])
                pos_c += 1
            else:
                print(negNum_m[neg_c])
                neg_c += 1
        if i % 2 == 1:
            if neg_c < neg:
                print(negNum_m[neg_c])
                neg_c += 1
            else:
                print(posNum_m[pos_c])
                pos_c += 1
