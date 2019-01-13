import os


# Выбор файла
def check_file():
    way = input('Введите название файла или путь к нему: ')
    while os.path.isfile(way) == False:
        way = input('Ошибка! Неверный ввод \nили такого файла не существует \
или неверное расширение файла.\n\
Для выхода нажмите Enter. Попробуйте ещё раз: ')
        
        if way == '':
            print()
            break
        
    return way


# Проверка наличия пути к файлу
def check_way(way):
    if way == '':
        print('Остутствует путь к файлу!')
        way = check_file()

    return(way)

# Проверка поля
def check_words(word):
    while len(word) > 17:
        word = input('Ошибка! Недопустимая длина строки (max 17). \n\
Для отмены нажмите Enter. Повторите ввод: ')
        if word == '':
            break
        
    return(word)
        

# Вывод всех записей из файла 
def content(way):    
    way = check_way(way)
    if way != '':
        f = open(way,'r')
        print()
        for line in f:
            print(line)
        f.close()
        print()

    return

# Создание нового набора записей(перезапись файла)
def new_content(way):
    way = check_way(way)
    if way != '':
        new_stroka = '0'
        f = open(way,'w')
        add_st(f)
        f.close()

    return

# Создание нового набора записей(новый файл)
def new_content_file():
    way = input('Введите название нового файла: ')
    new_stroka = '0'
    f = open(way,'w')
    add_st(f)
    f.close()

    return

# Выбор в "Создание нового набора записей"   
def new(way):
    a = input('Для записи нового файла напишите 1 \n\
Для перезаписи текущего - 2\n\
Для отмены - 0\n\
Ваш выбор: ')
    while a not in '0,1,2':
        a = input('Ошибка! Неверный ввод! Повторите ещё раз: ')

    if a == '1':
        new_content_file()

    if a == '2':
        new_content(way)

    return

# Добавление строки
def add_st(f):
    flag = 'Да'
    while flag.lower() != 'нет':
        word1 = input('Допустимая длина слова не более 17 символов. Введите продукт: ')
        word1 = check_words(word1)
        word2 = input('Допустимая длина слова не более 17 символов. Введите кол-во: ')
        word2 = check_words(word2)
        word3 = input('Допустимая длина слова не более 17 символов. Введите общую цену: ')
        word3 = check_words(word3)
        words = word1 + (18 - len(word1)) * ' ' + '| ' + \
                word2 +(17 - len(word2)) * ' ' + '| ' + word3
        
        f.write(words + '\n')
        flag = input('Вы желаете продолжить ввод записей?\n\
Да / Нет : ')
                     
    return()
    

# Добавление записи
def add_str(way):
    way = check_way(way)
    if way != '':
        f = open(way,'a')
        add_st(f)
        f.close()

    return
   
def check_field(word):
    column = ''
    while len(word) > 17 or word.lower() not in ('продукт','кол-во','общая цена'):
        word = input('Ошибка! Недопустимая длина строки (max 17)\
или неверно введено название поля. \n\
Для отмены нажмите Enter. Повторите ввод: ')
        if word == '':
            break
    if word.lower() == 'продукт':
        column = 0
    elif word.lower() == 'кол-во':
        column = 1
    elif word.lower() == 'общая цена':
        column = 2
        
    return(column,word)
    
# Поиск по одному полю
def search1(way):
    flag = True
    way = check_way(way)
    if way != '':
        f = open(way,'r')
        field = input('Для отмены нажмите Enter. Введите одно поле для поиска(продукт/кол-во/общая цена): ')
        field = field.lstrip().rstrip()
        column,field = check_field(field)
        word = input('Для отмены нажмите Enter. Введите слово для поиска в выбранном поле: ')
        word = check_words(word)
        if column != '' and word != '':
            print()
            for stroka in f:
                if word in stroka.split('|')[column]:
                    flag = False
                    print(stroka)
    
        f.close()

    if flag:
        print('\nПо данному запросу ничего не найдено.\n')

    return
    

# Поиск по двум полям
def search2(way):
    flag = True
    way = check_way(way)
    if way != '':
        f = open(way,'r')
        field1 = input('Для отмены нажмите Enter.Введите одно поле для поиска(продукт/кол-во/общая цена): ')
        column1,field1 = check_field(field1)
        word1 = input('Для отмены нажмите Enter.Введите слово для поиска в выбранном поле: ')
        word1 = check_words(word1)
        field2 = input('Для отмены нажмите Enter.Введите одно поле для поиска(продукт/кол-во/общая цена): ')
        column2,field2 = check_field(field2)        
        word2 = input('Для отмены нажмите Enter.Введите слово для поиска в выбранном поле: ')
        word2 = check_words(word2)

        if column1 != '' and column2 != '' and word1 != '' and word2 != '':
            print()
            for stroka in f:
                if word1 in stroka.split('|')[column1] and \
                    word2 in stroka.split('|')[column2]:                    

                    print(stroka)
                    
        f.close()

    if flag:
        print('\nПо данному запросу ничего не найдено.\n')

    return




way = ''
choice = 'ы'
while choice != '0':
    choice = input('Выберите функцию: \n\
    1) Выбор файла\n\
    2) Создание нового набора записей\n\
    3) Добавление записи\n\
    4) Вывод всех записей из файла\n\
    5) Поиск по одному полю\n\
    6) Поиск по двум поля\n\
    0) Выход\n\
    Ваш выбор: ')

    if choice == '1':
        way = check_file()

    if choice == '2':
        new(way)

    if choice == '3':
        add_str(way)                

    if choice == '4':
        content(way)
        
    if choice == '5':
        search1(way)
        
    if choice == '6':
        search2(way)
        
        
        
   
    
    
    
    











