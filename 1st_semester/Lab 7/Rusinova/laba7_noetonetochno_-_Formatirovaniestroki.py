# Задана поизв. строка q,
# 1) Удалить слова с большой буквы
# 2) Оставить между словами по одному пробелу
# 3) Напечатать получ строку и ее длину
# c использованиem массивов


# ВВОД ДАННЫХ
q = input()
Q = []
for i in q:
    Q.append(i)
n = len(q)

def UpperAlpha(x):
    return (65 <= ord(x) <= 90 or 1040 <= ord(x) <= 1071)

# ОБРАБОТКА СТРОКИ
i = 0
while i < n:
    if Q[i] == ' ':
        while i < n and Q[i] == ' ':
            Q[i] = ''
            i += 1
        i -= 1
        
    elif UpperAlpha(Q[i]) and (Q[i-1] == ' ' or Q[i-1] == ''):
        while i < n and Q[i] != ' ':
            Q[i] = ''
            i += 1
        i -= 1
        
    i+=1    

print(Q)
# ВЫВОД РЕЗУЛЬТАТА
print('Полученная строка: ')
k = 0
i = 0
f = 0
while i < n:
    if Q[i]:
        print(' '*f, end = '')
        k += 1*f
        f = 1
        while i < n and Q[i]:
            print(Q[i], end = '')
            k += 1
            i += 1
    i += 1
          
print()
print('Длина полученнной строки: ', k)
