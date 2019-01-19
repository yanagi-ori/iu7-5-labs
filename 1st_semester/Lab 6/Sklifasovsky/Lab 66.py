l = list(map(float,input("Введите массив: ").slpit))
colvo = len(l)
for i in range(colvo):
    c =1
    for j in range(colvo):
        if l[i] == l[j] and i != j:
            c += 1
        if max < c:
            max = c
print("Максимальное количество повторений = ", max)