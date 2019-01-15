# 1) Выбор файла
# 2) Создание нового набора записей = создание нового файла
# 3) Добавление записей - в текущий файл
# 4) Вывод всех записей из файла - из текущего
# 5) Поиск по одному полю (какие возможны поля для записи? Дата или название???)
# 6) Поиск по двум полям  (И дата, и название???)

# запись = запись в справочнике 

import os

# формирование меню
menuMain = '''
---------------------------------------------------
Доступные команды:

 1 - Открыть файл
 2 - Создать новый набор записей
---------------------------------------------------
'''

menuFile = '''
---------------------------------------------------
Доступные команды:

 1 - Добавить запись в текущий файл
 2 - Вывод всех записей из текущего файла
 3 - Поиск записи по одному полю
 4 - Поиск записи по двум полям

 z - Завершить работу с файлом и вернуться в главное меню
---------------------------------------------------
'''

info = '''

--------------------- (i) -------------------------
- Для вызова команды, введите ее номер
- Для вызова списка доступных команды, введите "m"
- Для завершения работы c программой, введите "q"
--------------------- (i) -------------------------
           
'''


def openFile(file,window):

    #print(os.getcwd())
    fileList = os.listdir(path=".")
    f = 0
    i = 1
    print('\nДоступные для открытия файлы: ')
    for file in fileList:
        if not '.py' in file:
            f = 1
            print(file)
    if not f:
        print('    Ни создано ни одного файла. Вы возвращены в главное меню.\n')
        return [file, window]
    fileName = input('Введите имя файла, который необходимо открыть: ')
    if not fileName[-4:] == '.txt':
        fileName = fileName.split('.')[0]+'.txt'
    
    try:
        file = open(fileName)
        
    except IOError:
        print('Не найдено файла с именем {}'.format(fileName))
        print('Вы возвращены в главное меню.')
        print(menuMain)

    else:
        window = 1
        print('Файл "{}" открыт.'.format(fileName))
        print('Для работы с файлом, введите номер команды...')
        print(menuFile)
    
    return [file,window]

def newFileSuccess(file, window):

    try:
        file = open(fileName, 'w')
        
    except IOError:
        print('Некорректное имя для файла')
        print('Вы возвращены в главное меню.')
        print(menuMain)

    else:
        window = 1
        mode = 1
        print('Файл "{}" создан.\n'.format(fileName))

        ans = input('Добавить новую запись? [y/n]: ')

        while ans and ans in 'yesYesдаДа':
            
            listTemp = addNote(file,window)
            file = listTemp[0]
            window = listTemp[1]

            ans = input('Добавить новую запись? [y/n]: ')
          
        print('Файл сформирован.\n')
        file.close()
        print('Для дальнейшей работы с файлом, введите номер команды...')
        print(menuFile)
        
    return [file,window]

def newFile(file, window):

    fileName = input('Имя нового файла: ')

    if not fileName:
        print('Некорректное имя для файла')
        print('Вы возвращены в главное меню.')
        print(menuMain)
        
    if not fileName[-4:] == '.txt':
        fileName = fileName.split('.')[0]+'.txt'
    filePath = os.getcwd()+'\\'+ fileName
    if os.path.isfile(filePath):
        
        ans = input(('Файл с указанным именем уже существует. Заменить? [y/n] : '))
        if ans in 'yesYesдаДа':

            lisT = newFileSuccess(file, window)
            file = lisT[0]
            window = lisT[1]

            return [file,window]
        
        else:
            print('Вы возвращены в главное меню.')
            return [file,window]
        
    else:
        lisT = newFileSuccess(file, window)
        file = lisT[0]
        window = lisT[1]

        return [file,window]

    




def addNote(file, window):
    
    if not (file and window):
        print('error')
        return [file,window]

    file = open(os.path.basename(file.name))
    lines = file.readlines()
    file.close()
    file = open(os.path.basename(file.name), 'w')
    for i in lines:
        file.write(i)
        
    name = input('Название книги: ')
    author = input('Автор книги: ')
    genre = input('Жанр книги: ')
    note = (name.strip().replace(' ','_') + ' ' + author.strip().replace(' ','_') +
            ' ' + genre.strip().replace(' ','_') + '\n')
    file.write(note)
    print('\nзапись добавлена в файл...\n')

        
    file.close()
    
    return [file,window]




def showAllNotes(file,window):

    if not (file and window):
        print('error')
        return [file,window]

    file = open(os.path.basename(file.name))
        
    print('Все записи файла:\n')
    f = 0

    for i in file:
        f = 1
        print('Название книги:', i.split(' ')[0].replace('_',' '))
        print('Автор книги:', i.split(' ')[1].replace('_',' '))
        print('Жанр книги:', i.split(' ')[2].replace('_',' '))
        print('\n')
    if not f:
        print('    В текущем файле нет ни одной записи.')
        
    file.close()
    
    return [file,window]


def search_oneAttr(file,window):
    
    if not (file and window):
        print('error')
        return [file,window]
    
    print('''1 - Название книги\n2 - Автор книги\n3 - Жанр книги''')
    
    file = open(os.path.basename(file.name))
    lines = file.readlines()
    file.close()

    attr = input('Введите номер аттрибута, по которому будет производиться поиск: ')
    if attr == '1':
        iS = 0
        
    elif attr == '2':
        iS = 1
        
    elif attr == '3':
        iS = 2
        
    else:
        print('\nНекорректное значение номера аттрибута.')
        print('Команда не может быть выполнена.\n')
        return [file,window]

    value = input('Введите слово (или его часть), по которому будет производиться поиск: ')
    results = []
    for line in lines:
        if value.lower() in line.strip('\n').split(' ')[iS].replace('_',' ').lower():
            results.append(line)
    if results:
        print('\nРезультаты поиска:\n')
        for rez in results:
            print('Название книги:', rez.split(' ')[0].replace('_',' '))
            print('Автор книги:', rez.split(' ')[1].replace('_',' '))
            print('Жанр книги:', rez.split(' ')[2].replace('_',' '))
            print('\n')
        return [file,window]
    else:
        print('\nСовпадений не найдено')
        return [file,window]

            

def search_twoAttr(file, window):

    if not (file and window):
        print('error')
        return [file,window]

    if not (file and window):
        print('error')
        return [file,window]
    
    print('''1 - Название книги\n2 - Автор книги\n3 - Жанр книги''')
    
    file = open(os.path.basename(file.name))
    lines = file.readlines()
    file.close()

    attr1 = input('Введите номер одного из аттрибутов, по которому будет производиться поиск: ')
    if attr1 == '1':
        iS1 = 0
        
    elif attr1 == '2':
        iS1 = 1
        
    elif attr1 == '3':
        iS1 = 2
        
    else:
        print('Некорректное значение номера аттрибута.')
        print('Команда не может быть выполнена.')
        return [file,window]

    value1 = input('Введите слово (или его часть), по которому будет производиться поиск: ')
    
    attr2 = input('Введите номер второго аттрибута, по которому будет производиться поиск: ')
    if attr2 == '1' and attr2 != attr1:
        iS2 = 0
        
    elif attr2 == '2' and attr2 != attr1:
        iS2 = 1
        
    elif attr2 == '3' and attr2 != attr1:
        iS2 = 2
        
    else:
        print('Некорректное значение номера аттрибута.')
        print('Команда не может быть выполнена.')
        return [file,window]

    value2 = input('Введите слово (или его часть), по которому будет производиться поиск: ')
    
    results = []
    for line in lines:
        if value1.lower() in line.split(' ')[iS1].replace('_',' ').lower() and value2.lower() in line.split(' ')[iS2].replace('_',' ').lower():
            results.append(line)
            
    if results:
        print('\nРезультаты поиска:\n')
        for rez in results:
            print('Название книги:', rez.split(' ')[0].replace('_',' '))
            print('Автор книги:', rez.split(' ')[1].replace('_',' '))
            print('Жанр книги:', rez.split(' ')[2].replace('_',' '))
            print('\n')
        return [file,window]
    else:
        print('\nСовпадений не найдено\n')
        return [file,window]

    
def quitFile(file, window):

    if not (file and window):
        print('error')
        return [file,window]
    
    print('\nзавершение работы с файлом...')
    file.close()
    file = None
    window = 0

    print('Вы возвращены в главное меню.')
    print(menuMain)
    
    return [file,window]


dictMain =  {'1': openFile, 
             '2': newFile
             }

dictFile =  {'1': addNote,
             '2': showAllNotes,
             '3': search_oneAttr,
             '4': search_twoAttr,
             'z': quitFile
             }


# входные данные
window = 0
file = None
print(info)
print(menuMain)
print('Для вызова справки, введите "i"')
s = input('Выполнить: ')

while s and not s in 'qQйЙ':
    
    if (s == '1' or s == '2') and not window:
        # выбор команды внутри главного меню
        listTemp = dictMain[s](file,window)
        file = listTemp[0]
        window = listTemp[1]
        
    elif (s == '1' or s == '2' or s == '3' or s == '4' or s == 'z') and window:
        # работа с файлом
        listTemp = dictFile[s](file,window)
        file = listTemp[0]
        window = listTemp[1]
        
    elif s in 'iIшШ':
        # показать справку
        print(info)
        
    elif s in 'mMмМ':
        # показать меню
        if window:
            print(menuFile)
        else:
            print(menuMain)
            
    else:
        # некорректное значение 
        print('Некорректное значение для вызова команды\n\n')

    print('Для вызова справки, введите "i"')
    s = input('Выполнить: ')

print('\nРабота завершена!\n')

    
        
    
