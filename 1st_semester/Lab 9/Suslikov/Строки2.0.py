from LIBR import check_float   #Импорт проверки чисел 

# Проверка ввода выбора функции редактирования текста

def check(x):
    while x not in '0,1,2,3,4,5,6,7':
        x = input('Ошибка! Введите число ещё раз: ')
    
    return x


znaki = ('.' ,',' , ':' , ';' , '...',' ')
znaki_predl = '.?!...'

# Проверка ввода слова

def word_check(a):
        
        while a.replace('-', '', 1).isalpha() == False:
            a = input('Ошибка! Введите СЛОВО. Для отмены нажмите Enter. ')
            if a == '':
                break    
        return a

# Нахождение максимальной длины строки

def max_len(text):
    maks_len = len(text[0])
    for i in range(1,len(text)):
        # print("---" + str(i) + " " + text[i] + " " + str(len(text[i])))
        if len(text[i]) > maks_len:
            maks_len = len(text[i])
    return maks_len

# Выравнивание по левому краю
def left(text):
    for i in range(len(text)):
        text[i] = ' '.join(text[i].split())

    return(text)

# Выравнивание по ширине

def width(text):
    maks_len = max_len(text)
    # print(maks_len)
    slov = 0    
    for i in range(len(text)):
        text[i] = ' '.join(text[i].split())
        # print('>' + text[i] + '<')
            
    for i in range(len(text)):
        space = maks_len - len(text[i])
        text[i] = text[i].split()
        for q in text[i]:
            slov += 1
        if slov == 1:
            kolvo = space // 2
            text[i] += [0]
            text[i][1] = text[i][0]
            text[i][0] = kolvo * ' '
        else:
            kolvo = space // (slov - 1)
            probel = kolvo * ' '
            for q in range(len(text[i])):
                text[i][q] += probel
                     
                if kolvo < space / (slov - 1):                     
                    text[i][q] += (space - kolvo * (slov - 1))  * ' '
                    kolvo =  100
                                                                       
        stroka = ' '.join(text[i])
        text[i]= stroka.strip()
        stroka = 0
        slov = 0
    

    return(text)



# Выравнивание по правому краю
def right(text):
    maks_len = max_len(text)
    for i in range(len(text)):
        text[i] = ' '.join(text[i].split())
        space = maks_len - len(text[i])
        text[i] = space * ' ' + text[i]

    return text

# Корректировка текста
def cor_text(text, last_choice):
    if last_choice == '1':
        width(text)
    elif last_choice == '2':
        left(text)
    elif last_choice == '3':
        right(text)

    return(text)


# Замена слова
def change_word(text,last_choice):
    nom = 0
    word = input('Введите слово, которое хотите заменить: ')
    word = word_check(word)
    wordz = input('Введите слово, на которое хотите заменить первое: ')
    wordz = word_check(wordz)
    for i in range(len(text)):
        text[i] = text[i].split()

        for slovo in text[i]:
            nom += 1

            if wordz != '' and (slovo == word  or slovo == word  + '.'  or slovo == word  + ',' \
                 or slovo == word  + ':' or slovo == word  + ';' or slovo == word  + '...'):
                
                for bukva in slovo:
                    if bukva in znaki:                        
                        znak = bukva
                nomz = nom - 1
                text[i][nomz] = wordz + znak
                  
        text[i] = ' '.join(text[i])        
        nom = 0
        znak = ''

        # Корректировка текста
    cor_text(text,last_choice)

    return(text)


# Удаление слова        
def del_word(text,last_choice):
    znak = ''
    nom = 0
    ud_slovo = input('Введите удаляемое слово: ')
    ud_slovo = word_check(ud_slovo)
    for i in range(len(text)):
        text[i] = text[i].split()

        for slovo in text[i]:
            nom += 1

            if slovo == ud_slovo  or slovo == ud_slovo  + '.'  or slovo == ud_slovo  + ',' \
                or slovo == ud_slovo  + ':' or slovo == ud_slovo  + ';' \
                or slovo == ud_slovo  + '...':
                    for bukva in slovo:
                        if bukva in znaki:
                            znak = bukva
                    nomud = nom - 1
                    text[i][nomud] = znak

        text[i] = ' '.join(text[i])
        nom = 0
        znak = ''
        
        # Корректировка текста
        cor_text(text,last_choice)

    return(text)


# Вычисление выражений с * и /
def calc(text):
    change = False 
    chislo1 = ''
    chislo2 = ''
    for i in range(len(text)):
        stroka_old = text[i]
        stroka_new = text[i].split()

        for j in range(len(stroka_new)):
            n = 0
            for k in range(len(stroka_new[j])):
                k += n

                # Отделение  чисел от знаков пробелом

                if (stroka_new[j][k] in '*/') and len(stroka_new[j]) > 1:
                    if k == 0 and check_float(stroka_new[j][1:]):
                        stroka_new[j] = stroka_new[j][0] + ' ' \
                            + stroka_new[j][1:]
                        n += 1
                    elif k == (len(stroka_new[j]) - 1) and \
                            check_float(stroka_new[j][0:len(stroka_new[j]) - 1]):
                        stroka_new[j] = stroka_new[j][:-1] + ' ' \
                            + stroka_new[j][-1:]
                        n += 1

                    elif check_float(stroka_new[j][0:k])  and \
                        check_float(stroka_new[j][k + 1:]):
                            stroka_new[j] = stroka_new[j][0:k] + ' ' \
                               + stroka_new[j][k] + ' ' + stroka_new[j][k + 1:]
                            n += 2

        stroka_new = ' '.join(stroka_new).split()
        n = 0


        # Вычисление выражения
           
        for j in range(len(stroka_new)):
            j -= n
            if stroka_new[j] in '*/':
                try:
                    chislo1 = float(stroka_new[j - 1])
                    chislo2 = float(stroka_new[j + 1])
                except (ValueError, IndexError):
                    pass

                else:
                    if chislo2 == 0:
                        print('Ошибка! На ноль делить нельзя!')
                        pass
                        

                    elif stroka_new[j] == '/' and chislo2 != 0:
                        
                        stroka_new[j- 1] = str(chislo1 / chislo2)
                        n += 2
                        del stroka_new[j], stroka_new[j]
                        change = True
                    elif stroka_new[j] == '*':
                        stroka_new[j - 1] = str(chislo1 * chislo2)
                        n += 2
                        del stroka_new[j], stroka_new[j]
                        change = True

        if change:
            text[i] = ' '.join(stroka_new)

        else:
            text[i] = stroka_old

    # Корректировка текста
    cor_text(text,last_choice)

    return(text)   


# Нахождение самого короткого слова в предложении
def min_word(text):
    min_dlina_slova = 1000
    min_slovo = ''
    sl = ''
    nomer = 0
    for i in range(len(text)):
        for bukva in text[i]:
                
            if bukva.isalpha() or bukva == '-':
                sl += bukva                    
            else:
                dlina_slova = len(sl)

                if dlina_slova < min_dlina_slova and dlina_slova > 0:
                    min_dlina_slova = dlina_slova
                    min_slovo = sl
                sl = ''
 

            if bukva in znaki_predl and (pred_bukva.isalpha() == True or pred_bukva == ' '):
                nomer += 1
                print('В ',nomer,'-м предложении самое короткое слово - ',min_slovo)
                min_dlina_slova = 1000                   

            pred_bukva = bukva

    return(text)


text = ['В полях белеет белый',
        'снег. А 12*20 /5 воды уж весной',
        'шумят. Бегут и будят',
        'сонный брег. Бегут, а блещут,',
        'а гласят. Это 2  / 5* 3 * 6 / 0 стихотворение',
        'сочинил кто-то не я. А кто-то за меня.']


print('Исходный текст\n')
for q in text:
    print(q)

print()
print()

# Вывод списка функций
choice = 'a'
last_choice = 0

while choice != '0':
    if choice in ('1', '2', '3'):
        last_choice = choice
    choice = input('Выберите функцию:\n\
    0) Выход\n\
    1) Выравнивание по ширине.\n\
    2) Выравнивание по левому краю.\n\
    3) Выравнивание по правому краю.\n\
    4) Замена во всем тексте одного слова другим.\n\
    5) Удаление заданного слова из текста.\n\
    6) Замена арифметических выражений, состоящих из умножения и деления, на \
результат их вычисления.\n\
    7) Найти самое короткое слово в каждом предложении.\n\
    Ваш выбор: ')
    # choice = check(choice)
    print()

    # Выравнивание по ширине

    if choice == '1':
        width(text)
                
    # Выравнивание по левому краю

    if choice == '2':
        left(text)
                       
   # Выравнивание по правому краю
    
    if choice == '3':
        right(text)
       
    # Замена слова
    
    if choice == '4': 
        change_word(text,last_choice)

                                
    # Удаление слова
    
    if choice == '5':
        del_word(text,last_choice)


    # Замена арифметических выражений
    
    if choice == '6':
        text = calc(text)

    # Нахождение самого короткого слова в предложении
    
    if choice == '7':
        min_word(text)


    
    print('\nВаш текст\n')
    for q in text:
        print(q)
    print()        






