print('Введите элементы массива через пробел: ')
orig_m = list(map(float, input().split()))
len_m = len(orig_m)
b = 1
aver = 0
for i in range(2, len_m, 2):
    orig_m[b] = orig_m[i]
    b += 1
for i in range(b):
    aver += orig_m[i]
for i in range(len_m - 1, len_m - b, -1):
    orig_m[i] = None
aver //= 2
aver_i = b // 2
last = orig_m[aver_i]
orig_m[aver_i] = aver
if b%2 == 0:
    orig_m[b] = ''
for i in range(aver_i+1, b+1):
    cur = orig_m[i]
    orig_m[i] = last
    last = cur
if b%2 == 0:
    orig_m[b+1] = ''
for i in range(len_m):
    print(orig_m[i])
