# 1 - Выравнивание по ширине
# 2 - Выравнивание по левому краю
# 3 - Выравнивание по правому краю
# 4 - Замена во всем тексте одного слова другим
# 5 - Удаление заданного слова из текста
# 6 - Замена арифметических выражений, сост-х из умножения и деления
#     на результат
# 7 - Найти предложения в которых гласные буквы чередуются с согласными.

from copy import deepcopy

text  =   ['Lfjkйой                рвгвоfh fjлввраgj       вшарвfig',
           'iuрLfjkйойiuri     (12*ы5)/11   fugiвщшащвufgi. Rt',
           'ifарво    онgiguiu fgifgчсоочuif    (3*4)/7 3*5   3*6   dffпппнfi',
           'djfijdfjdi.   Lfjkйой     Yкttuut789 ',
           'hifi. figi   qIqiq/\	\\\Iqiq    Iqiqi    qiqu.         ',
           'T       12*6/7*8     yyyi Uuuu. 0/0 Lfjkйой  ',
           'tyuyiyy.       ']

menu = '''Допустимые команды:
    1 - Выравнивание по ширине
    2 - Выравнивание по левому краю
    3 - Выравнивание по правому краю
    4 - Замена во всем тексте одного слова другим
    5 - Удаление заданного слова из текста
    6 - Замена арифметических выражений, сост-х из умножения и деления
        на результат
    7 - Найти предложения в которых гласные буквы чередуются с согласными.'''



    
# поиск максимального кол-ва символов в строке
def findMaxLen(text):
    norm(text)
    global maxLen      # максимальное кол-во символов 
    for i in text:
        lenTemp = len(i)
        maxLen = max(lenTemp, maxLen)         
    return maxLen

# форматирование текста
def norm(a):
    for i in range(len(a)):
        a[i] = a[i].split()
        s = ''
        #print(a[i])
        for j in range(len(a[i])-1):
            s += a[i][j]+' '
        if a[i]:
            s += a[i][-1]
        else:
            s = ' '
        a[i] = s


# выравнивание по ширине
def alignWidth():

    global maxLen
    global oneWord_i
    global text
    global f
    
    maxLen = findMaxLen(text)

    for i in range(len(text)):
        # можно вставить пробелы между словами
        if ' ' in text[i]:                    
            textTemp = text[i].split()
            delta = (maxLen - (len(text[i])-len(textTemp)+1))
        # можно вставить пробелы только между буквами одного слова
        else:                                 
            textTemp = [j for j in text[i]]
            delta = (maxLen - len(text[i]))
            if not i in oneWord_i:
                oneWord_i.append(i)

        proms = len(textTemp) - 1    
        delta_prom = delta//(proms)                            
        sTemp = ''
        
        for j in range(proms):
            sTemp += (textTemp[j]+' '*delta_prom)
        sTemp += (' '*(delta-delta_prom*proms) + textTemp[-1])
        
        text[i] = sTemp
        print(text[i], end='          \{}\n'.format(len(text[i])))

    f = 1
    return 


# выравнивание по левому краю
def alignLeft():

    global maxLen
    global oneWord_i
    global text
    global f
    
    maxLen = findMaxLen(text)

    for i in range(len(text)):
        
        s = ''
        textTemp = text[i].split()
        
        if ' ' in text[i] and not i in oneWord_i:
            for j in range(len(textTemp)-1):
                s += textTemp[j]+' '
        else:
            for j in range(len(textTemp)-1):
                s += textTemp[j]
                
        s += textTemp[-1]
        text[i] = s
        sF = '{:'+str(maxLen)+'}'
        text[i] = sF.format(text[i])
        print(text[i])

    f = 2
    return


# выравнивание по правому краю
def alignRight():

    global maxLen
    global oneWord_i
    global text
    global f
    
    maxLen = findMaxLen(text)
    for i in range(len(text)):
        
        s = ''
        textTemp = text[i].split()

        if ' ' in text[i] and (not i in oneWord_i):
            for j in range(len(textTemp)-1):
                s += textTemp[j]+' '
        else:
            for j in range(len(textTemp)-1):
                s += textTemp[j]
                
        s += textTemp[-1]
        text[i] = s
        sF = '{:>'+str(maxLen)+'}'
        text[i] = sF.format(text[i])
        print(text[i])

    f = 3
    return



# замена слова на другое слово
def replaceWord():
    global text
    global f
    
    oldW = input('Введите, какое слово необходимо заменить: ').strip()
    if len(oldW.split())>1:
        print('Введено некорректное значение для слова')
        return
    newW = input('Введите, на какое слово необходимо заменить "{}": '.format(oldW)).strip()
    if len(newW.split())>1:
        print('Введено некорректное значение для слова')
        return
    print('\n\n')
    fl = 0
    for i in range(len(text)):
        line = text[i]
        if oldW in line:
            j = 0
            while j < len(line):
                if line[j] == oldW[0] and (j==0 or line[j-1] == ' '):
                    jT = j
                    while jT < len(line) and jT-j < len(oldW) and line[jT] == oldW[jT-j]:
                        jT += 1
                    if jT-j == len(oldW) and (jT-1 == len(line)-1 or line[jT] == ' '):
                        fl = 1
                        line = line[:j] + newW + line[jT:]
                    #j = jT-1
                    j = len(line[:j])+len(newW)-1
                j += 1
        text[i] = line
    if not fl:
        print('Не найдено заданного слова в тексте\n')
    if f:
        d[str(f)]()
    else:
        for i in text:
            print(i)
    return

# удаление заданного слова из текста
def deleteWord():
    global text
    global f
    
    oldW = input('Введите, какое слово необходимо удалить: ').strip()
    if len(oldW.split())>1:
        print('Введено некорректное значение для слова')
        return
    print('\n\n')
    fl = 0
    for i in range(len(text)):
        line = text[i]
        if oldW in line:
            j = 0
            while j < len(line):
                if line[j] == oldW[0] and (j==0 or line[j-1] == ' '):
                    jT = j
                    while jT < len(line) and jT-j < len(oldW) and line[jT] == oldW[jT-j]:
                        jT += 1
                    if jT-j == len(oldW) and (jT-1 == len(line)-1 or line[jT] == ' '):
                        fl = 1
                        if jT-1 != len(line)-1:
                            line = line[:j] + line[jT+1:]
                            k = j
                        elif j != 0 and jT-1 == len(line)-1:
                            line = line[:j-1] + line[jT:]
                            k = j-1
                        elif j == 0 and jT-1 == len(line)-1:
                            line = line[:j] + line[jT:]
                            k = j
                    #j = jT-1
                    j = len(line[:k])-1
                j += 1
        text[i] = line
    if not fl:
        print('Не найдено заданного слова в тексте\n')
    if f:
        d[str(f)]()
    else:
        for i in text:
            print(i)
    return

# замена арифм. операции на рез-т
def resultExpr():
    global text
    global f
    for p in range(len(text)):
        line = text[p]
        i = 0
        iS = 0
        while i < len(line):
            if line[i] in '()+-0123456789' and (i == 0 or line[i-1] == ' '):
                #s = ''
                a = []
                st = []
                iS = i
                while i < len(line) and line[i] != ' ':  # подстрока с выражением
                    if line[i].isdigit():
                        sD = ''
                        while i < len(line) and line[i].isdigit():
                            #s += line[i]
                            sD += line[i]
                            i += 1
                        a.append(int(sD))
                        i -= 1
                    elif line[i] in '*/':
                        if st and st[-1] != '(':
                            x = st.pop()
                            #s += x
                            a.append(x)
                        st.append(line[i])
                    elif line[i] == '(':
                        st.append(line[i])
                    elif line[i] == ')':
                        x = ''
                        if st:
                            x = st.pop()
                        while x != '(' and st:
                            #s += x
                            a.append(x)
                            x = st.pop()
                        if st:
                            st.pop()
                    else:
                        while i< len(line) and line[i] != ' ':
                            i+=1
                        #s = ''
                        st = []
                        a = []
                        break
                    i += 1
                if st:
                    x = st.pop()
                    #s += x
                    a.append(x)
                if a:
                    res = ''
                    #print(a)
                    # посчитай
                    aT = []
                    result = ''
                    while a:
                        x = a.pop(0)
                        #print(a, '///', aT, '///', x)
                        if str(x)[0] in '01234567890':
                            aT.append(x)
                        elif x == '*':
                            res = aT.pop(-2)*aT.pop()
                            aT.append(res)
                        elif x == '/':
                            try:
                                res = aT.pop(-2)/aT.pop()
                                aT.append(res)
                                #print(a, aT, res)
                            except ZeroDivisionError:
                                res = 'error'
                                break
                    #print(res)
                    if res == 'error':
                        result = res
                    elif res:
                        result = '{:5g}'.format(res)
                    if result:    
                        text[p] = line[:iS] + result + line[i:]
                        i = len(line[:iS]) - 1 + len(result)
                        line = text[p]
                #s = ''
                st = []
                a = []
            i += 1

    if f:
        d[str(f)]()
    else:
        for i in text:
            print(i)
    return


# поиск предложения удв условию 7
def findSent():
    global text
    vowels = 'aeiouаяуюоёэеыи'
    flAll = 0
    sText = ''
    for i in text:
        sText += i
    sText = sText.split('.')
    norm(sText)
    
    for stroka in sText:
        if stroka[0].lower() in vowels:
            k = 1
        elif stroka[0].isalpha():
            k = 0
        else:
            k = len(s)-1
            
        j = k
        jN = k+1
        fl = 0
        while j < len(stroka)-1 and jN < len(stroka):
            fl = 1
            if stroka[j].isalpha() and not stroka[j].lower() in vowels:
                if stroka[jN].lower() in vowels:
                    j = jN+1
                    jN = j+1
                elif not stroka[jN].isalpha():
                    jN += 1
                else:
                    fl = 0
                    break
            elif not stroka[j].isalpha():
                j += 1
                jN = j+1
            else:
                fl = 0
                break
       
        if fl:
            print(stroka,'.', sep = '')
            flAll = 1
            
    if not flAll:
        print('В данном тексте нет таких предложений')
    return
    
d = {'1': alignWidth,
     '2': alignLeft,
     '3': alignRight,
     '4': replaceWord,
     '5': deleteWord,
     '6': resultExpr,
     '7': findSent }


listLens = []      # кол-ва непробельных символов в каждой строке
maxLen = 0         # максимальное кол-во непробельных символов в строке
oneWord_i = []
f = 0              #флаг равнения




# вывод исходного текста и его форматирование
textCopy = deepcopy(text)
print('Заданный текст:')
print()
for i in range(len(text)):
    print(text[i])


print('\n\n')
print(menu)
print('\n\n')

print('(i)-Чтобы выполнить команду, введите ее номер в меню')
print('(i)-Чтобы снова вызвать меню, введите "m"')
print('(i)-Чтобы вернуь текст к первоначальному виду, введите "b"')
print('(i)-Чтобы завершить обработку текста, введите "q"')
s = input('Выполнить: ')

while s and s != 'q' and s != 'Q' and s != ' ':
    if s == 'm' or s == 'M' or s == 'м' or s == 'М':
        print(menu)
    elif s == 'b' or s == 'B' or s == 'б' or s == 'Б':
        text = deepcopy(textCopy)
        print('Текст возвращен к исходному состоянию:\n')
        for i in text:
            print(i)
    else:
        try:
            print('\n\n')
            d[s]()
        except KeyError:
            print('Введено некорректное значение для команды')
        
    print('\n\n')
    print('(i)-Чтобы снова вызвать меню, введите "m"')
    print('(i)-Чтобы вернуь текст к первоначальному виду, введите "b"')
    print('(i)-Чтобы завершить обработку текста, введите "q"')
    s = input('Выполнить: ')

print()
print('Обработка завершена!')
print('Преобразованный текст:')
print()
for i in text:
    print(i)

