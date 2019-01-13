# Богатырев Иван
# Массивы. Первая задача

# -----------------------------------------------------------------------------
# orig_m - исходный массив, orig_m_len - длина исходного массива,
# new_m - новый массив, new_m_len - длина нового массива,
# i - шаг для нового массива, k - шаг для исходного массива,
# negative - флаг для определения существования отрицательного числа в массиве,
# del_point - номер отрицательного элемента
# -----------------------------------------------------------------------------


from sys import exit

from iu7_basemodule import start_check

baka = False
check = ''
final = []
n = input('Задача №1\nВведите размер массива: ')
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

orig_m_len = len(orig_m)
del_point = orig_m_len

# Высчитывются первый отрицательный элемент
for i in range(orig_m_len):
    if float(orig_m[i]) < 0:
        del_point = i
        break

new_m = []
for i in range(0, del_point, 2):
    new_m.append(orig_m[i])
    # print(orig_m[i])

print(new_m)