a = [[0]*8,
     [1, 1, 1, 0, 0, 0, 0, 0],
     [1, 0, 1, 0, 0, 0, 0, 0],
     [1, 1, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0]
     ]

count = 0
for i in range(len(a)):
    finish = 0
    for j in range(len(a[i])):
        if a[i][j] == 1:
            start = finish
            finish = j
            if start == 0 and finish - start > 1:
                count += finish - start - 1
            if start != 0:
                count += finish - start - 1
print('Матрица')
for i in range(len(a)):
    print(a[i])
print('\nКоличество нулей внутри фигуры:', count)
