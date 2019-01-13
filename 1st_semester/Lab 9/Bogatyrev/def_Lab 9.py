text = ['   Текст для     тестирования 4 + 5 + 6', 'лабораторной         работы по',
        'программированию. Понедельник 5 - 1 - 0 день недели,',
        'а             декабрь 14',
        '-            2 месяц. Эту работу         пишу уже',
        '1 + 1 недели. И             все это очень        продолжительное время',
        'она не работает.']

main_length = len(text)

# Подготовка текста
for row in range(main_length):
    text[row] = text[row].replace('+', ' + ')
    text[row] = text[row].replace('-', ' - ')
    temp_list = text[row].split()
    for i in range(len(temp_list)):
        if temp_list[i] == '':
            del temp_list[0]
    text[row] = ' '.join(temp_list)

# Начало задания
spm = (' '.join(text)).replace('!', '.')
spm = spm.replace('?', '.')
spm = spm.split('. ')
check = [0, 0]
# Поиск самого длинного предложения
for i in range(len(spm)):
    spm[i] = spm[i].split()
    if len(spm[i]) > check[0]:
        check = [len(spm[i]), i]
# Для поиска самого короткого
for i in range(len(spm)):
    if len(spm[i]) < check[0]:
        check = [len(spm[i]), i]
spm = spm[check[1]]
check = [0, 0]
# Поиск самого длинного слова
for i in range(len(spm)):
    if len(spm[i]) > check[0]:
        check = (len(spm[i]), i)
print(spm[check[1]])

