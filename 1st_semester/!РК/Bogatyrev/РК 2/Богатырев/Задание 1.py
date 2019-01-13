# 66 Вариант


def enter():
    string = str(input())
    if string.replace(' ', '').replace('\n', '') == '':
        print('Введены недопустимые данные! Попробуйте  еще раз.')
        enter()
    return string


def by_char(word):
    mas_by_char = []
    for char in word:
        if char != ' ':
            mas_by_char.append(char)
    return mas_by_char


process = True
print('Введите строку S: ', end='')
S = enter()
S = by_char(S)

while process:
    print('Введите строку F: ', end='')
    F = enter()
    F = by_char(F)

    for i in range(len(F)):
        for j in range(len(S)):
            if S[j] == F[i]:
                S[j], F[i] = '', ''

    if ''.join(F) == '':
        print('Из строки S можно составить строку F')
    else:
        print('Из строки S нельзя оставить строку F')

    ans = str(input('Ввести еще одну строку F? (Y/N) '))
    if ans.upper() in ['N', 'Н', 'Т']:
        process = False
