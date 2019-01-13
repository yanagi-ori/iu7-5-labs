# Методы сортировки
import random


# Сортировка выбором
# Сортировка выбором — здесь, чтобы отсортировать массив, находим элемент с минимальным значением,
# затем сравниваем его со значением первой неотсортированной позиции.
# Если этот элемент меньше, то он становится новым минимумом и их позиции меняются.
def ssort(array):
    for i in range(len(array)):
        indxMin = i
        for j in range(i+1, len(array)):
            if array[j] < array[indxMin]:
                indxMin = j
        tmp = array[indxMin]
        array[indxMin] = array[i]
        array[i] = tmp
    return array


# Сортировка вставками
# - из массива последовательно берется каждый элемент
# - вставляется в его отсортированную часть(например в начале массива)
def isort(array):
    for i in range(len(array)):
        v = array[i]
        j = i
        while (array[j-1] > v) and (j > 0):
            array[j] = array[j-1]
            j = j - 1
        array[j] = v
        print(array)
    return array


# Метод пузырька
# Суть алгоритма в том, что совершается несколько проходов по массиву.
# При проходе последовательно сравниваются пары элементов в массиве
# и в случае несоответствия выбранному порядку меняются местами.
# Если пары элементов находятся в верном порядке, то ничего не происходит.
# В результате первого прохода максимальный элемент окажется в конце,
# то есть всплывет словно пузырек. Затем все повторяется до того момента
# пока весь массив не будет отсортирован.
# Последний проход будет по отсортированному массиву.

def bubble_sort(array):
    a = array
    for i in range(len(a), 0, -1):
        for j in range(1, i):
            if a[j-1] > a[j]:
                tmp = a[j-1]
                a[j-1] = a[j]
                a[j] = tmp
                print(a)
    return a


def bubble_sort_2(array):
    n = 1
    while n < len(array):
        for i in range(len(array) - n):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        n += 1
    return array


# Метод шелла
# Идея заключается в том, чтобы просматривать элементы беря каждый i тый элементы (начало откуда угодно).
# В результате мы получаем массив где каждый i-тый элемент отсортирован.
# Повторяя такую операцию с использованием меньших i,
# заканчивая 1 результатом будет отсортированный массив.
def Shell(array):
    t = int(len(array) / 2)
    while t > 0:
        for i in range(len(array) - t):
            j = i
            while j >= 0 and array[j] > array[j + t]:
                array[j], array[j + t] = array[j + t], array[j]
                j -= 1
        t = int(t/2)
    return array


# Метод быстрой сортировки
# Идея алгоритма заключается в том, что выбирается опорный элемент,
# относительно которого будет происходит сортировка.
# Равные и бОльшие элементы помещаются справа, меньшие – слева.
# Затем к полученным подмассивам рекурсивно применяются два первых пункта.
def QuickPas(array, aL, aR):
    left, right = aL, aR
    mid = (array[left] + array[(left + right) / 2] + array[right]) / 3
    while mid:
        right -= 1
        if left <= right:
            if array[left] > array[right]:
                array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1
    if right > aL:
        QuickPas(array, aL, right)
    if left < aR:
        QuickPas(array, left, aR)
    return array


def quick_sort(nums):
    if len(nums) <= 1:
        return nums
    else:
        q = random.choice(nums)
        s_nums = []
        m_nums = []
        e_nums = []
        for n in nums:
            if n < q:
                s_nums.append(n)
            elif n > q:
                m_nums.append(n)
            else:
                e_nums.append(n)
        return quick_sort(s_nums) + e_nums + quick_sort(m_nums)

"""
верхнем левом столбце найти первые две цифры года;
В найденной строке найти столбец с последними двумя цифрами номера года;
В месячных календарях (расположены слева и справа) найти строку, соответствующую числу месяца;
На пересечении строки числа месяца и столбца года найти день недели.
"""