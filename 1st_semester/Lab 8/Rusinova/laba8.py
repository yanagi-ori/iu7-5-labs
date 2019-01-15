# 1 - Выравнивание по ширине
# 2 - Выравнивание по левому краю
# 3 - Выравнивание по правому краю
# 4 - Замена во всем тексте одного слова другим
# 5 - Удаление заданного слова из текста
# 6 - Замена арифметических выражений, сост-х из умножения и деления
#     на результат
# 7 - Найти предложения в которых гласные буквы чередуются с согласными.

from copy import deepcopy

text  =   ['Lfjkйойрвгвоfh fjлввраgj     вшарвfig',
           'iuрвнараfiuri   (12*ы5)/11   fugiвщшащвufgi. Rt',
           'ifарвоонgiguiu fgifgчсоочuif (3*4)/7 3*5 3*6   dffпппнfi',
           'djfijdfjdi.   Rff     Yкttuut789 ',
           'hfifgi   IyyЫy    iii iu ',
           'T 12*6/7*10  yyyi Uuuu   .  Ttre  ',
           'tyuyiyy. T.',
           'qwerty.']

textCopy = ['Lfjkйойрвгвоfh fjлввраgj     вшарвfig',
           'iuрвнараfiuri   (12*ы5)/11   fugiвщшащвufgi. Rt',
           'ifарвоонgiguiu fgifgчсоочuif (3*4)/7 3*5 3*6   dffпппнfi',
           'djfijdfjdi.   Rff     Yкttuut789 ',
           'hfifgi   IyyЫy    iii iu ',
           'T 12*6/7*10  yyyi Uuuu   .  Ttre  ',
           'tyuyiyy. T.',
           'qwerty.']

menu = '''Допустимые команды:
    1 - Выравнивание по ширине
    2 - Выравнивание по левому краю
    3 - Выравнивание по правому краю
    4 - Замена во всем тексте одного слова другим
    5 - Удаление заданного слова из текста
    6 - Замена арифметических выражений, сост-х из умножения и деления
        на результат
    7 - Найти предложения в которых гласные буквы чередуются с согласными.'''
    
print()
# Формирование меню
print(menu)
print()
print('Чтобы вызвать команду, введите ее номер.'
      'Чтобы завершить обработку текста, введите символ "q".')
f = 0      #нет равнения
fn = False #нет нормализации

def normalize(st):
    i = 0
    if st[0] == ' ':
            while st[i] == ' ':
                i += 1
    j = -1
    if st[-1] == ' ':
        while st[j] == ' ':
            j -= 1
    j = len(st) + j
    return st[i:j+1]
    
def alignWidth():
    global maxLen
    global text
    global f
    if maxLen == 0:
        for i in text:
            if len(i) > maxLen:
                maxLen = len(i)
    for x in range(len(text)):
        stTemp = ''
        st = text[x]
        if ' ' in st:
            Len = 0
            stMass = st.split()
            for i in range(len(stMass)):
                for j in stMass[i]:
                    Len += 1
            delta = maxLen - Len  # недостающие пробелы
            prom = len(stMass) - 1
            delta_i = delta//(prom)
            for i in range(prom):
                stTemp += (stMass[i] + ' '*delta_i)
            stTemp += (' '*(delta-delta_i*prom) + stMass[-1])
            text[x] = stTemp
            print(text[x], end = '              | ')
            print( Len+delta_i*prom+(delta-delta_i*prom), '/', maxLen )
        else:
            delta = maxLen - len(st)     # недостающие пробелы
            prom = len(st)-1
            delta_i = delta//prom
            for i in range(prom):
                stTemp += (st[i]+' '*delta_i)
            stTemp += (' '*(delta-delta_i*prom) + st[-1])
            text[x] = stTemp
            print(text[x], end = '              | ')
            print( (prom+1)+delta_i*prom+(delta-delta_i*prom), '/', maxLen )
    f = 1
    return 

def alignLeft():
    global text 
    global maxLen
    if maxLen == 0:
        for i in text:
            if len(i) > maxLen:
                maxLen = len(i)
    sForm = '{:'+str(maxLen)+'}'
    for i in range(len(text)):
        sTemp = ''
        for j in text[i].split():
            sTemp += (j+' ')
        print(sForm.format(i))
    f = 2
    return

def alignRight():
    global text 
    global maxLen
    global f
    if maxLen == 0:
        for i in a:
            if len(i) > maxLen:
                maxLen = len(i)
    sTemp = '{:>'+str(maxLen)+'}'
    for i in text:
        print(sTemp.format(i))
    f = 3
    return

def replaceWord():
    global text
    print('4')
    return
def deleteWord():
    global text
    print('5')
    return
def resultExpr():
    global text
    print('6')
    return
def findSent():
    global text
    print('7')
    return
    
d = {'1': alignWidth,
     '2': alignLeft,
     '3': alignRight,
     '4': replaceWord,
     '5': deleteWord,
     '6': resultExpr,
     '7': findSent }

()
print('Заданный текст:')
for i in range(len(text)):
    text[i] = text[i].split()
    print(text[i])

print()
print('(i)-Чтобы снова вызвать меню, введите "m"')
print('(i)-Чтобы вернуь текст к первоначальному виду, введите "b"')
s = input('Выполнить: ')
maxLen = 0

while s and s != 'q' and s != 'Q' and s != ' ':
    print()
    if s == 'm' or s == 'M' or s == 'м' or s == 'М':
        print(menu)
    elif s == 'b' or s == 'B' or s == 'б' or s == 'Б':
        text.deepCopy(textCopy)
        for i in text:
            print(i)
    else:
        if not fn:
            for i in range(len(text)):
                text[i] = normalize(text[i])
        d[s]()
    print()
    print('(i)-Чтобы снова вызвать меню, введите "m"')
    print('(i)-Чтобы вернуь текст к первоначальному виду, введите "b"')
    s = input('Выполнить: ')

print()
print('Обработка завершена!')
print('Преобразованный текст:')
print('Текст')


    
