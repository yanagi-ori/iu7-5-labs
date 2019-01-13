import sys
from os import system

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


def process():
    for row in range(main_length):
        text[row] = text[row].replace('+', ' + ')
        text[row] = text[row].replace('-', ' - ')
        temp_list = text[row].split()
        for i in range(len(temp_list)):
            if temp_list[i] == '':
                del temp_list[0]
        text[row] = ' '.join(temp_list)

    global max_l
    max_l = 0
    for j in range(len(text)):
        if len(text[j]) > max_l:
            max_l = len(text[j])


def menu():
    print('1 - Выравнивание по ширине',
          '\n2 - Выравнивание по левому краю',
          '\n3 - Выравнивание по правому краю',
          '\n4 - Замена во всем тексте одного слова другим',
          '\n5 - Удаление заданного слова из текста',
          '\n6 - Замена арифметических выражений, состоящих из сложения и '
          'вычитания, на результат их вычисления',
          '\n7 - Найти предложение с максимальным количеством слов, в которых '
          'гласные чередуются с согласными',
          '\n0 - Выход')
    ans = input()
    if ans.isdigit():
        if 0 <= int(ans) <= 7:
            ans = int(ans)
            if ans == 1:
                center()
            if ans == 2:
                left_side()
            if ans == 3:
                right_side()
            if ans == 4:
                replace()
            if ans == 5:
                delete()
            if ans == 6:
                arithmetic()
            if ans == 7:
                special()
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


def form():
    ans = int(mode)
    if ans == 1:
        center()
    if ans == 2:
        left_side()
    if ans == 3:
        right_side()


def center():
    process()
    for row in range(main_length):
        local_len = len(text[row])
        if local_len == max_l:
            print(text[row])
        else:
            words = text[row].split()
            words_num = len(words)
            if words_num == 1:
                text[row] = ' ' * ((max_l - local_len) // 2) + ''.join(words) + ' ' * ((max_l - local_len) // 2)
                print(text[row])
            else:
                dif = ((max_l - local_len) % (words_num - 1) + 1)
                if dif != 0:
                    st = words[0] + ' ' * ((max_l - local_len) // (words_num - 1) + 1) + words[1]
                    for m in range(2, len(words)):
                        if dif > 1:
                            st += (' ' * ((max_l - local_len) // (words_num - 1) + 2)) + words[m]
                            dif -= 1
                        else:
                            st += (' ' * ((max_l - local_len) // (words_num - 1) + 1)) + words[m]

                    print(st)
                    text[row] = st
                else:
                    spaces = ' ' * ((max_l - local_len) // (words_num - 1) + 1)
                    text[i] = spaces.join(text[i].split(' '))
                    print(text[i])
    global mode, raw
    mode = 1
    raw = False
    input('\nГотово!\nНажмите Enter, чтобы продолжить')
    system('cls')
    menu()


def left_side():
    process()
    for i in range(main_length):
        print(text[i])

    global mode, raw
    mode = 2
    raw = False

    input('\nГотово!\nНажмите Enter, чтобы продолжить')
    system('cls')
    menu()


def right_side():
    process()
    for i in range(main_length):
        local_length = len(text[i])
        if local_length == max_l:
            print(text[i])
        else:
            spaces = ' ' * (max_l - local_length)
            st = spaces + text[i]
            print(st)
            text[i] = st
    global mode, raw
    mode = 3
    raw = False
    input('\nГотово!\nНажмите Enter, чтобы продолжить')
    system('cls')
    menu()


def replace():
    temp = text
    old_word = input('Введите слово, которое хотите заменить: ')
    if old_word == '':
        input('Введены неверные данные!\nНажмите Enter и попробуйте снова.')
        system('cls')
        replace()
    new_word = input('Введите слово, которым хотите замменить: ')
    if new_word == '':
        input('Введены неверные данные!\nНажмите Enter и попробуйте снова.')
        system('cls')
        replace()
    for i in range(main_length):
        row = text[i].split()
        for j in range(len(row)):
            if row[j].upper() == old_word.upper():
                text[i] = new_word.join(text[i].split(row[j]))
            if row[j].replace('.', '').upper() == old_word.upper():
                text[i] = (new_word + '.').join(text[i].split(row[j]))
            if row[j].replace(',', '').upper() == old_word.upper():
                text[i] = (new_word + ',').join(text[i].split(row[j]))
    if raw is False:
        process()
        form()
    for i in range(len(text)):
        print(text[i])
    if temp == text:
        print('(Замен не произведено)')
    input('\nГотово!\nНажмите Enter, чтобы продолжить')
    system('cls')
    menu()


def delete():
    temp = text
    check = False
    word = input('Введите слово, которое хотите удалить: ')
    if word == '':
        input('Введены неверные данные!\nНажмите Enter и попробуйте снова.')
        delete()
    for i in range(main_length):
        row = text[i].split()
        for j in range(len(row)):
            if row[j].replace('.', '').replace(',', '').upper() == word.upper():
                text[i] = ''.join(text[i].split(' ' + row[j]))
                text[i] = ''.join(text[i].split(row[j] + ' '))
                text[i] = ''.join(text[i].split(row[j]))
                check = True
    for i in range(len(text)):
        print(text[i])
    if raw is False:
        process()
        form()
    if len(' '.join(temp)) == len(' '.join(text)):
        print('\n(Замен не произведено)')
    input('\nГотово!\nНажмите Enter, чтобы продолжить')


def arithmetic():
    process()
    ar = False
    last_line = None
    for row in range(main_length):
        line = text[row].split()
        for i in range(len(line) - 1):
            if line[0] == '+' or line[0] == '-':
                if last_line is None:
                    pass
                else:
                    for d in range(len(last_line)-1, 0 - 1, -1):
                        if last_line[d] == '':
                            d -= 1
                        else:
                            break
                    a = easy_check(last_line[d].replace(',', '', 1))

                    for d in range(i + 1, len(line) + 1):
                        if line[d] == '':
                            d += 1
                        else:
                            break
                    b = easy_check(line[d].replace(',', '', 1))
                    if a[1] is False and a[0].isdigit() and b[1] is False and b[0].isdigit():
                        ar = True
                        if line[i] == '+':
                            line[i] = str(round(float(a[0]) + float(b[0])))
                        elif line[i] == '-':
                            line[i] = str(round(float(a[0]) - float(b[0])))
                        if ar:
                            last_line[- 1] = ''
                            line[i + 1] = ''
                            text[row-1] = ' '.join(last_line)

            elif line[i] == '+' or line[i] == '-':
                for d in range(i-1, 0-1, -1):
                    if line[d] == '':
                        d += 1
                    else:
                        break
                a = easy_check(line[d].replace(',', '', 1))
                for d in range(i+1, len(line)+1):
                    if line[d] == '':
                        d += 1
                    else:
                        break
                b = easy_check(line[d].replace(',', '', 1))
                if a[1] is False and a[0].isdigit() and b[1] is False and b[0].isdigit():
                    ar = True
                    if line[i] == '+':
                        line[i] = str(round((float(a[0]) + float(b[0]))))
                    elif line[i] == '-':
                        line[i] = str(round((float(a[0]) - float(b[0]))))
                    if ar:
                        process()
                        if line[i - 1] == '':
                            line[i - 2] = ''
                        else:
                            line[i - 1] = ''
                        line[i + 1] = ''
        text[row] = ' '.join(line)
        last_line = text[row].split()
    if raw is False:
        process()
        form()
    for i in range(main_length):
        print(text[i])
    input('\nГотово!\nНажмите Enter, чтобы продолжить')
    system('cls')
    menu()


def special():
    process()
    spm = (' '.join(text)).replace('!', '.')
    spm = spm.replace('?', '.')
    spm = spm.split('. ')
    wis = 0
    max_wis = [0, 0]
    i = 0
    for sntc in range(len(spm)):
        wis = 0
        i = 0
        i += 1
        temp = spm[sntc].split()
        for word in temp:
            next_cons = False
            next_vow = False
            abort = False
            if len(word) == 1:
                continue
            else:
                if word[0].upper() in vow:
                    next_cons = True
                    next_vow = False
                elif word[0].upper() in cons:
                    next_cons = False
                    next_vow = True
                else:
                    abort = True
                for i in range(len(word)-1):
                    lit = word[i+1].upper()
                    if next_cons and lit in cons:
                        next_cons = False
                        next_vow = True
                    elif next_vow and lit in vow:
                        next_cons = True
                        next_vow = False
                    elif next_cons and lit in vow or next_vow and lit in cons:
                        abort = True
                        break
                if abort is False:
                    wis += 1
            if wis > float(max_wis[0]):
                max_wis = wis, sntc

    print('Искомое предложение:', spm[max_wis[1]])
    input('\nГотово!\nНажмите Enter, чтобы продолжить')
    system('cls')
    menu()


# Множества гласных и согласных букв
vow = ['А', 'О', 'У', 'Ы', 'Э', 'Я', 'Е', 'Ё', 'Ю', 'И']
cons = ['Б', 'В', 'Г', 'Д', 'Й', 'Ж', 'З', 'К', 'Л', 'М', 'Н', 'П',
        'Р', 'С', 'Т', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ']
non = {'Ь', 'Ъ'}
num = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '+', '.'}
ar = False
raw = True

# Предварительная обработка
"""
text = ['Скрипка издергалась, упрашивая, ',
        'и вдруг разревелась',
        'так по-детски,',
        'что барабан не выдержал: ',
        'Хорошо, хорошо, хорошо!',
        'А сам устал, 2+3',
        'не дослушал скрипкиной речи, 1',
        '+3 шмыгнул на горящий Кузнецкий',
        'и ушел.']
"""

# text = [' Текст для тестирования 4 + 5', 'лабораторной работы по', 'программированию. Понедельник 1 - 0 день недели',]

text = ['   Текст для     тестирования 4 + 5 + 6', 'лабораторной         работы по',
        'программированию. Понедельник 5 - 1 - 0 день недели',
        'а             декабрь 14',
        '-            2 месяц. Эту работу             пишу уже',
        '1 + 1 недели. И             все это        продолжительное время',
        'она не работает.']
main_length = len(text)
max_l = 0
mode = 2
for i in range(len(text)):
    print(text[i])

# Старт программы
menu()