import os
from pathlib import Path
def srezprobelov(m):
    count = 0
    for x in m:
        ln = len(x)
        i, j = 0, 0
        k, k1 = 0, 0
        while x[i] == ' ':
            i += 1
            k += 1
        while x[ln - 1 - j] == ' ':
            k1 += 1
            j += 1
        m[count] = None
        m[count] = x[k:ln - k1]
        count += 1
    return m
def width(path):
    f = open(path, 'r')
    m = []
    for line in f:
        m += [line.strip()]
    f.close()
    m = width1(m)
    return m
def width1(m):
    m = srezprobelov(m)
    t = ''
    q = 0
    for x in m:
        t += (x + ' ')
    t = t.split()
    for i in t:
        if q < len(i):
            q = len(i)
        
    t = []
    for x in m:
        t += [x.split()]
    new = []
    for x in t:
        p = ''
        for i in x:
            p += (i + ' '*(q - len(i)) + ' ')
        new += [p]
    return new

        

def createnew(path):
    print()
    f = open(path, 'w')
    f.write('товар цена кол-во' + '\n')
    choice = None
    while choice != '0':
        if choice != '0':
            print('Вводите строки в формате:\n'
                  'Товар Цена Количество\n'
                  'Образец: Замки 250 5\n')
            row = ''
            znaki = '.,:...; '
            vvod = False
            while not vvod:
                product = input('Ввдетие название продукта > ')
                if product != '' and product not in znaki:
                    row += (product + ' ')
                    vvod = True
                else:
                    print('Некорректный ввод продукта') 
                    vvod = False
            print('Вводить нужно только цифры. Цена товара и количество' 
                  'должны быть целыми числами')
            vvod = False
            while not vvod:
                number1 = input('Ввдетие цену товара > ')
                try:
                    number = int(number1)
                except:
                    print('Вы неправильно ввели цену товара. Введите целое число')
                else:
                    row += (number1 + ' ')
                    vvod = True
            vvod = False
            while not vvod:
                number2 = input('Введите кол-во товара > ')
                try:
                    number = int(number2)
                except:
                    print('Вы неправильно ввели количество товара')
                else:
                    row += (number2 + ' ')
                    vvod = True
            print(row)
            f.write(row + '\n')   
                    
        print('\nЕсли хотите закончить - введите 0,'
            '\nНет - нажмите Enter\n')
        choice = input()
    f.close()

def seeout(path):
    f = open(path, 'r')
    for line in f:
        print(line.rstrip())
    f.close()

def addtext(path):
    print()
    f = open(path, 'a')
    print('Вводите строки в формате: '
          'Товар Цена Количество\n'
          'Образец: Замки 250 5\n')
    znaki = '.,:...; '
    row = ''
    product = input('Ввдетие название продукта > ')
    if product != '' and len(product.split()) == 1 and product not in znaki:
        row += (product + ' ')
        number1 = input('Ввдетие цену товара > ')
        number2 = input('Введите кол-во товара > ')
        try:
            number = int(number1)
            number = int(number2)
        except:
            print('Некорректная строка, повторите ввод\n')
        else:
            row += (number1 + ' ')
            row += (number2 + ' ')
            print(row)
            f.write(row + '\n')
    else:
        print('Неккоректное слово')
    f.close()

def fineonefield(path):
    f = open(path, 'r')
    print()
    word = input('Выберите поле (слово): ')
    znaki = '.,:...; '
    if not word.isdigit() and word != '' and len(word.split()) == 1 and word not in znaki:
        k = None    
        print()
        for line in f:
            if word in line.split():
                print(line)
                k = 1
        if k is None:
            print('Вы выбрали неверное поле')
    else:
        print('Нужно ввести именно товар')
    f.close()

def findtwofields(path):
    f = open(path, 'r')
    print()
    word1 = input('Выберите первое поле (слово): ')
    word2 = input('Выберите второе поле (цена или количество): ')
    znaki = '.,:...; '
    if not word1.isdigit() and word1 != '' and len(word1.split()) == 1 and word1 not in znaki:
        if word2.isdigit() and word2 != '' and len(word2.split()) == 1 and word2 not in znaki:
            k = None
            print()
            for line in f:
                if word1 in line.split() and word2 in line.split():
                    print(line, end='')
                    k = 1
            if k is None:
                print('Вы выбрали неверные поля')
        else:
            print('Вы ввели неверную цену или количество')
    else:
        print('Нужно ввести именно товар')
    f.close()


path = ''
m = None
choice=None
while choice != '0':
    print('\n1 - Выбор файла',
          '\n2 - Создание нового файла',
          '\n3 - Добавление записи',
          '\n4 - Вывод всех записей файла',
          '\n5 - Поиск по одному полю',
          '\n6 - Поиск по двум полям',
          '\n7 - Выровнять файл по столбцам',
          '\n0 - Выход')

    choice = input('Выбор: ')

    if choice == '0':
        print('Выход.')
    
    elif choice == '1':
        temp_path = input('\nВведите имя файла или путь до него: ').strip()
        # Проверка на существование
        if os.path.isfile(temp_path):
            print('Файл выбран')
            path = temp_path
        else:
            print('Файл не найден')
    elif choice == '2':
        check_path = input('Введите название файла > ')

        if Path(check_path).suffix == '.txt':
            path = check_path
            createnew(path)
        else:
            print('Вы неправильно создали файл, повторите снова')

    elif choice == '3':
        if path == '':
            print('\nСначала введите или создайте файл')
        else:
            addtext(path)
    elif choice == '4':
        if path == '':
            print('\nСначала выберите или создайте файл')
        else:
            print()
            seeout(path)

    elif choice == '5':
        if path == '':
            print('\nСначала введите или создайте файл')
        else:
            fineonefield(path)

    elif choice == '6':
        if path == '':
            print('\nСначала введите или создайте файл')
        else:
            findtwofields(path)
    elif choice == '7':
        a = width(path)
        f = open(path, 'w')
        for line in a:
            f.write(line + '\n')
        f.close()
        seeout(path)
    else:
        print('Введенного номера нет ',choice)



input('\nНажмите Enter.')