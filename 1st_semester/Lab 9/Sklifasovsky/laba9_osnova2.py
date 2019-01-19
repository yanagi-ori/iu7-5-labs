# Склифасовский Денис ИУ7-15
# Меню стандартных преобразований текста

import os
from os import system

# Убирает пробелы вначале
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


# Удобный вывод
def vivod(m):
    max_l = 0
    for i in range(len(m)):
        if len(m[i]) > max_l:
            max_l = len(m[i])
    print('━' * max_l)
    for x in m:
        print(x)
    print('━' * max_l)
    input('\nГотово!\nНажмите Enter, чтобы продолжить')
    print()
def vivod2(m):
    max_l = 0
    for i in range(len(m)):
        if len(m[i]) > max_l:
            max_l = len(m[i])
    print('━' * max_l)
    for x in m:
        print(x)
    print('━' * max_l)
    print()


# Выравнивание по ширине
def width(m):
    ln_max = 0
    t = []
    srezprobelov(m)
    for x in m:
        if (len(x) > ln_max):
            ln_max = len(x)
    for x in m:
        buf = []
        m1 = []
        j = 0
        st = ''
        del_ln = ln_max - len(x)
        for i in range(len(x)):
            if (x[i] == ' '):
                buf.append(i)
        for i in range(len(buf)):

            num = buf[i]
            if del_ln // len(buf) != 0:

                st = x[j:num] + ' ' * (del_ln // len(buf)) + ' '
                m1.append(st)
            else:
                st = x[j:num] + ' '
                m1.append(st)
            j = num + 1

        m1.append(' ' * (del_ln % len(buf)))
        num = buf[len(buf) - 1] + 1
        m1.append(x[num:])
        t += [''.join(m1)]

    m1 = None
    buf = None
    return t


def check(m):
    try:
        m = int(m)
        return m
    except (IndexError, ValueError):
        pass

# Выравнивание по левому краю
def left(m):
    m = vosvrat(m)
    m = srezprobelov(m)
    return m


# Выравнивание по праваму краю
def right(m):
    m = vosvrat(m)
    ln_max = 0
    m = srezprobelov(m)
    for x in m:
        if len(x) > ln_max:
            ln_max = len(x)
    text1 = []
    for x in m:
        del_ln = ln_max - len(x)
        x = ' ' * del_ln + x
        text1 += [x]
    return text1


# Заменяет слово
def change(m):
    w1 = input('Введите слово, которое хотите заменить: ')
    w2 = input('Введите слово, которым хотите замменить: ')
    if w1 != '' and w2 != '':
        k1, k2 = 0, 0
        for i in w1:
            k1 += 1
        for i in w2:
            k2 += 1
        if k1 > 1 and k2 > 0:
            m = zamena1(m, w1, w2)
        elif k1 <= 1 and w1 not in slova and k2 <= 1 and w2 not in slova:
            print(w1, 'и', w2, 'не являются словами')
        elif k1 <= 1 and w1 not in slova:
            print(w1, 'не является словом')
        elif k2 <= 1 and w2 not in slova:
            print(w2, 'не является словом')

        else:
            m = zamena1(m, w1, w2)
    else:
        print('Вы ничего не ввели')
    return m
# Функция для замены
def zamena1(m, w1, w2):
    zn = ''
    st = ''
    t = []
    for x in m:
        x = x.split()
        nom = 0
        for slovo in x:
            if slovo == w1 or slovo == w1 + ' ' or slovo == w1 + '.' or slovo == w1 + ',' \
                or slovo == w1 + ':' or slovo == w1 + ';':
                for bukva in slovo:
                    if bukva in znaki:
                        zn = bukva
                slovo = w2 + zn
            st += slovo + ' '
        t += [st]
        st = ''
        zn = ''
    if d == 'w':
        t = width(t)
    elif d == 'r':
        t = right(t)
    elif d == 'l':
        t = left(t)
    return t


# Удаляет слово
def delete(m):
    k = 0
    word = input('Введите слово, которое нужно удалить > ')
    for x in word:
        k += 1
    if k > 1:
        m = delete1(m, word)
    elif k == 1 and word in slova:
        m = delete1(m, word)
    else:
        print(word, 'не является словом')
    return m
# Функция для удаления
def delete2(m, word):
    q = []
    for i in range(len(m)):
        row = ''.join(text[i].split(' ' + word))
        row = ''.join(row.split(word + ' '))
        row = ''.join(row.split(word))
        q += [row]
    return q
def delete1(m, word):
    #word = input('Введите слово')
    zn = ''
    st = ''
    t = []
    for x in m:
        x = x.split()
        nom = 0
        for slovo in x:
            if slovo == word or slovo == word + ' ' or slovo == word + '.' or slovo == word + ',' \
                or slovo == word + ':' or slovo == word + ';':
                for bukva in slovo:
                    if bukva in znaki:
                        zn = bukva
                slovo = zn
            st += slovo + ' '
        t += [st]
        st = ''
        zn = ''
    if d == 'w':
        t = width(t)
    elif d == 'r':
        t = right(t)
    elif d == 'l':
        t = left(t)
    return t


# Заменяет арифметические выражения на их результат
def summa1(m):
    mas = '.e0123456789'
    t = []
    #srezprobelov3

    for x in m:
        s = []
        k = 0
        plus = []
        for i in range(len(x)):
            if x[i] == '+' or x[i] == '-':
                plus.append(i)
        if (len(plus) > 0):
            for i in range(len(plus)):
                num, buf1, buf2 = plus[i], plus[i], plus[i]
                j = 0
                p = 1
                while j == 0:
                    if x[buf1 - 1] in mas:
                        buf1 -= 1
                    else:
                        j = 1
                while p == 1:
                    if x[buf2 + 1] in mas:
                        buf2 += 1
                    else:
                        p = 0
                if x[num] == '-':
                    s.append(str(int(x[buf1:num]) - int(x[num + 1:buf2 + 1])))
                else:
                    s.append(str(int(x[buf1:num]) + int(x[num + 1:buf2 + 1])))
                # print(s)
                # print(x[:buf1-1] + ' ' +x[buf2+1:])
                x = x[:buf1 - 1] + ' ' + s[k] + x[buf2 + 1:]
                k += 1
        t += [x]
    if d == 'w':
        t = width(t)
    elif d == 'r':
        t = right(t)
    elif d == 'l':
        t = left(t)
    return t
def summa(m):
    check_eval = False

    for k in range(len(m)):
        temp = m[k]
        t = m[k].split()

        # Отделяем знаки от цифр
        for i in range(len(t)):
            l = 0
            for z in range(len(t[i])):
                z += l
                if t[i][z] in '+-' and len(t[i]) > 1:
                    if z == 0 and check(t[i][1:]):
                        t[i] = t[i][0] + ' ' + t[i][1:]
                        l += 1
                    elif z == (len(t[i]) - 1) and check(t[i][0:len(t[i]) - 1]):
                        t[i] = t[i][:-1] + ' ' + t[i][-1]
                        l += 1
                    elif check(t[i][0:z]) and check(t[i][z + 1:]):
                        t[i] = t[i][0:z] + ' ' + t[i][z] + ' ' + t[i][z + 1:]
                        l += 2

        t = ' '.join(t).split()
        l = 0

        # Вычисление
        for i in range(len(t)):
            i -= l
            if t[i] in '+-':
                try:
                    a = int(t[i - 1])
                    b = int(t[i + 1])
                except (IndexError, ValueError):
                    pass
                else:
                    if t[i] == '-':
                        t[i - 1] = str(a - b)
                        l += 2
                        del t[i], t[i]
                        check_eval = True
                    elif t[i] == '+':
                        t[i - 1] = str(a + b)
                        l += 2
                        del t[i], t[i]
                        check_eval = True
        if check_eval:
            m[k] = ' '.join(t)
        else:
            m[k] = temp
        if d == 'w':
            m = width(m)
        elif d == 'r':
            m = right(m)
        elif d == 'l':
            m = left(m)
    return m, check_eval

# Находит самое короткое слово в самом длинном предложении
def slovo(m):
    t = ''
    for x in m:
        t += (x + ' ')
    t = t.split('.')
    del t[len(t)-1]
    q = 0
    ik = []
    p = 0
    for x in t:
        x += ' '
        k = 0
        slovo = ''
        for c in x:
            if c != ' ':
                slovo += c
            else:
                if slovo != '':
                    if len(slovo) > p:
                        p = len(slovo)
                    k += 1
                    slovo = ''
        if k > q:
            q = k
            ik = [x]
    o = None
    for x in ik:
        slovo = ''
        for c in x:
            if c != ' ':
                slovo += c
            else:
                if slovo != '':
                    if len(slovo) < p:
                        p = len(slovo)
                        o = slovo
                    slovo = ''
    return o


# Оставляет по 1 пробелу между словами
def vosvrat(m):
    t = []
    for x in m:
        x = x.split()
        st = ''
        for i in x:
            st += (i + ' ')
        x = st
        t += [x]
    return t

d = None

if True:

    text1 = [
        '       Заметался пожар голубой, позабылись',
        '  родимые дали. 5-3 . В первый   5-3+2',
        'раз я запел про любовь. 5,+5 В первый',
        ' раз отрекаюсь скандалить. 5-3а Был я',
        'весь как запущеный 6 - 3 сад,',
        'был на женщин 6+1 и зелия ',
        'падок. Разонравилось 2+2 + 2 пить я плясать',
        'и терять свою жизнь без оглядки.'
        ]
    znaki = '.,;: '
    slova = 'явксоуиабаоэЯВКСОУИАБАОЭ'

    text = [
        'Заметался пожар голубой,',
        'Позабылись родимые дали. 5-3 .',
        'В первый раз я запел про любовь,',
        'В первый раз отрекаюсь скандалить.',
        'Был я весь как запущенный сад,',
        'Был на женщин и зелие падкий.',
        'Разонравилось пить и плясать',
        'И терять свою жизнь без оглядки.',
        'Мне бы только смотреть на тебя,',
        'Видеть глаз злато-карий омут,',
        'И чтоб, прошлое не любя,',
        'Ты уйти не смогла к другому.',
        'Поступь нежная, легкий стан,',
        'Если б знала ты сердцем упорным,',
        'Как умеет любить хулиган,',
        'Как умеет он быть покорным.'
    ]

    max_l = 0
    main_l = len(text)
    for i in range(len(text)):
        if len(text[i]) > max_l:
            max_l = len(text[i])
    srezprobelov(text)

# Меню
if True:
    choice = None
    while choice != '0':

        print('1 - Выравнивание по ширине',
              '\n2 - Выравнивание по левому краю',
              '\n3 - Выравнивание по правому краю',
              '\n4 - Замена во всем тексте одного слова другим',
              '\n5 - Удаление заданного слова из текста',
              '\n6 - Замена арифметических выражений, состоящих из сложения и '
              'вычитания, на результат их вычисления',
              '\n7 - Найти самое короткое слово в самом длинном предложении',
              '\n8 - Посмотреть исходный текст',
              '\n0 - Выход')

        choice = input('Выбор: ')

        if choice == '0':
            print('Выход.')

        elif choice == '1':
            system('cls')
            d = 'w'
            text = width(text)
            vivod(text)

        elif choice == '2':
            system('cls')
            d = 'l'
            text = left(text)
            vivod(text)

        elif choice == '3':
            system('cls')
            d = 'r'
            text = right(text)
            vivod(text)

        elif choice == '4':
            system('cls')
            vivod2(text)
            print()
            text = change(text)
            vivod(text)

        elif choice == '5':
            system('cls')
            vivod2(text)
            print()
            text = delete(text)
            vivod(text)

        elif choice == '6':
            system('cls')
            text, eval_check = summa(text)
            print()
            if eval_check:
                vivod(text)
            else:
                print('Корректные выражения не обнаружены\n')
                    

        elif choice == '7':
            system('cls')
            vivod2(text)
            print()
            t = slovo(text)
            print('Самое короткое слово в самом длинном предложении: ', t)
            input('\nГотово!\nНажмите Enter, чтобы продолжить')
            print()

        elif choice == '8':
            system('cls')
            print()
            vivod(text)

        else:
            print('Введенного номера нет ', choice)

    input('\nНажмите Enter.')
