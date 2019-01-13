import sys
from os import system, path
from pathlib import PurePosixPath

from iu7_basemodule import start_check


def easy_check(x):
    skip = x
    temp = start_check(x)
    if temp[1] is False and temp[0].isdigit() is True:
        x = [skip, temp[1]]
        return x
    else:
        x = [skip, temp[1]]
        return x


def menu():
    print('1 - Выбор файла',
          '\n2 - Создание нового нвбора записей',
          '\n3 - Добавление записи',
          '\n4 - Вывод всех записей из файла',
          '\n5 - Поиск по одному полю',
          '\n6 - Поиск по двум полям',
          '\n0 - Выход')
    ans = input()
    if ans.isdigit():
        if 0 <= int(ans) <= 7:
            ans = int(ans)
            if ans == 1:
                open_file()
            if ans == 2:
                new_file()
            if ans == 3:
                add_new()
            if ans == 4:
                read_file()
            if ans == 5:
                search_by_one()
            if ans == 6:
                search_by_two()
            if ans == 0:
                sys.exit()
        else:
            input('Выбран отсутствующий пункт!\nНажмите Enter и попробуйте снова.')
            system('cls')
            menu()

    else:
        input('Введены неверные данные!\nНажмите Enter и попробуйте снова.')
        system('cls')
        menu()


def open_file():
    global file_path, file, glob_col
    file_path = input('Введите путь до файла: ').strip()
    if path.isfile(file_path) and PurePosixPath(file_path).suffix in suf:
        input('Готово!')
    else:
        print('Ошибка, файл не выбран')
        open_file()
    try:
        file = open(file_path)
    except IOError:
        input('Указанный файл не найден!\nНажмите Enter и попробуйте еще раз.')
        open_file()
    file.close()
    file = open(file_path)
    for line in file:
        if line.replace('\n', '').replace(' ', '') == '':
            continue
        else:
            sep_line = line.split('; ')
            glob_col = len(sep_line)
            break
    file.close()
    system('cls')
    menu()


def new_file():
    global file_path, glob_col
    file_path = input('Введите путь до нового файла: ')
    if file_path == '':
        input('Введены неверные данные!\nНажмите Enter и попробуйте снова.')
        new_file()
    try:
        file = open(file_path)
    except IOError:
        if PurePosixPath(file_path).suffix in suf:
            file = open(file_path, 'w')
            ans = input('Заполнить новый файл? ')
            if ans.upper() in pos_ans:
                add_new()
            elif ans.upper() in neg_ans:
                print('OK')
                system('cls')
                file.close()
                menu()
            else:
                input('Введены неверные данные!\nНажмите Enter и попробуйте снова.')
                new_file()
            input('Готово!')
        else:
            input('Введены неверные данные!\nНажмите Enter и попробуйте снова.')
            new_file()
    else:
        input('Указанный файл уже существует.\nНажмите Enter и попробуйте еще раз')
        new_file()

    for line in file:
        if line.replace('\n', '').replace(' ', '') == '':
            continue
        else:
            sep_line = line.split('; ')
            glob_col = len(sep_line)
            break
    file.close()
    system('cls')
    menu()


def add_new():
    if file_path is None:
        input('Путь до файла не задан!\nИспользуйте первый или второй пункт для выбора файла.\nНажмите Enter...')
        system('cls')
        menu()
    else:
        file = open(file_path, 'a+')
        file.read()
        print('Добавляйте новые записи в одном формате.')
        new_value = input('Введите новую запись (разделение через ";"): ')
        if len(new_value.split('; ')) == glob_col:
            file.write(new_value+'\n')
            ans = input('Готово!\nДобавить еще одну? (Y/N) ')
            file.close()
            if ans.upper() in pos_ans:
                add_new()
            elif ans.upper() in neg_ans:
                print('OK')
                system('cls')
                menu()
            else:
                input('Введены неверные данные!\nНажмите Enter и попробуйте снова.')
                add_new()
        else:
            input('Введены неверные данные!\nНажмите Enter и попробуйте снова.')
            add_new()
            file.close()


def read_file():
    if file_path is None:
        input('Путь до файла не задан!\nИспользуйте первый или второй пункт для выбора файла.\nНажмите Enter...')
        system('cls')
        menu()
    else:
        file = open(file_path)

        if file.read().replace('\n', '') == '':
            print('Файл пуст')
        else:
            file.close()
            file = open(file_path)
            # line = file.readline()
            for line in file:
                if line.replace('\n', '').replace(' ', '') == '':
                    continue
                else:
                    sep_line = line.split('; ')
                    col_num = len(sep_line)
                    separate = '-' * (31 * col_num + 1)
                    print(separate)
                    cur_line = '|'
                    for part in sep_line:
                        cur_line += '{:^30}'.format(part.replace('\n', '')) + '|'
                    print(cur_line)
                    print(separate)
                    for line in file:
                        sep_line = line.split('; ')
                        cur_line = '|'
                        col = 1
                        for part in sep_line:
                            cur_line += '{:^30}'.format(part.replace('\n', '')) + '|'
                            if col == col_num:
                                break
                            col += 1
                        print(cur_line)
                    print(separate)
        file.close()
    input('Готово!')
    system('cls')
    menu()


def search_by_one():
    if file_path is None:
        input('Путь до файла не задан!\nИспользуйте первый или второй пункт для выбора файла.\nНажмите Enter...')
        system('cls')
        menu()
    else:
        file = open(file_path)
        sep_line = file.readline().split('; ')
        col_num = len(sep_line)
        print('Доступные поля:')
        for i in range(len(sep_line)):
            print(str(i+1) + ' - ' + sep_line[i])
        try:
            column = int(input('Введите номер поля для поиска: '))
        except ValueError:
            print('Введены неверные данные!\nНажмите Enter и попробуйте снова.')
            search_by_one()
        search = input('Введите поисковой запрос: ')
        separate = '-'*(21*col_num+1)
        result = False
        print(separate)
        for line in file:
            sep_line = line.split('; ')
            if sep_line[column - 1].replace('\n', '') == search:
                result = True
                cur_line = '|'
                trigger = 1
                for part in sep_line:
                    cur_line += '{:^20}'.format(part.replace('\n', '')) + '|'
                    if trigger == glob_col:
                        break
                    trigger += 1
                print(cur_line)
        if result:
            print(separate + '\nЗапрос выполнен.', end=' ')
        else:
            print(' '*((21*col_num+1-40)//2) + 'По данному запросу ничего не найдено...')
            print(separate)
        input('Для продолжения нажмите Enter.')
        file.close()
    system('cls')
    menu()


def search_by_two():
    if file_path is None:
        input('Путь до файла не задан!\nИспользуйте первый или второй пункт для выбора файла.\nНажмите Enter...')
        system('cls')
        menu()
    else:
        file = open(file_path)
        sep_line = file.readline().split('; ')
        col_num = len(sep_line)
        print('Доступные поля:')
        for i in range(len(sep_line)):
            print(str(i + 1) + ' - ' + sep_line[i])
        try:
            column1 = int(input('Введите номер первого поля для поиска: '))
        except ValueError:
            print('Введены неверные данные!\nНажмите Enter и попробуйте снова.')
            search_by_one()
        search1 = input('Введите поисковой запрос для этого поля: ')
        try:
            column2 = int(input('Введите номер поля для поиска: '))
        except ValueError:
            print('Введены неверные данные!\nНажмите Enter и попробуйте снова.')
            search_by_one()
        search2 = input('Введите поисковой запрос для этого поля: ')
        separate = '-' * (21 * col_num + 1)
        result = False
        print(separate)
        for line in file:
            sep_line = line.split('; ')
            if sep_line[column1-1].replace('\n', '') == search1 \
                    and sep_line[column2-1].replace('\n', '') == search2:
                result = True
                cur_line = '|'
                trigger = 1
                for part in sep_line:
                    cur_line += '{:^20}'.format(part.replace('\n', '')) + '|'
                    if trigger == glob_col:
                        break
                    trigger += 1
                print(cur_line)
        if result:
            print(separate + '\nЗапрос выполнен.', end=' ')
        else:
            print(' ' * ((21 * col_num + 1 - 40) // 2) + 'По данному запросу ничего не найдено...')
            print(separate)
        input('Для продолжения нажмите Enter.')
        file.close()
    system('cls')
    menu()


file_path = None
suf = {'.txt', '.rtf', '.data', '.h', '.doc', '.docx', '.text',
       '.lyx', '.html', '.htm', '.odt', '', '.py'}
neg_ans = {'N', 'Н', 'Т'}
pos_ans = {'Y', 'Д'}
menu()
glob_col = 1
