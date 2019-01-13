from sys import exit


################################################
# start_check(temp, baka) - проверка от дурака #
# easy_check(x) - упорщенная версия проверки   #
# std_round(x) - округление до 7 значащих цифр #
################################################


def start_check(temp, baka=False):
    pre_check = temp.split('e')
    if len(pre_check) > 2:
        baka = True
    elif len(pre_check) == 2:
        if pre_check[0] == '' or pre_check[1] == '':
            baka = False
        else:
            temp1 = list(pre_check[0])
            if temp1[0] == '.' or temp1[0] == '-' or temp1[0] == "+":
                del temp1[0]
            temp1 = ''.join(temp1)

            temp1 = temp1.split(' ')
            if len(temp1) > 1:
                baka = True
            temp1 = ''.join(temp1)
            temp1 = temp1.split('-')
            if len(temp1) > 1:
                baka = True
            temp1 = ''.join(temp1)
            temp1 = temp1.split('.')
            if len(temp1) > 2:
                baka = True
            temp1 = ''.join(temp1)

            temp2 = list(pre_check[1])
            if temp2[0] == '-' or temp2[0] == "+":
                del temp2[0]
            temp2 = ''.join(temp2)
            temp2 = temp2.split(' ')
            if len(temp2) > 1:
                baka = True
            temp2 = ''.join(temp2)
            temp2 = temp2.split('-')
            if len(temp2) > 1:
                baka = True
            temp2 = ''.join(temp2)
            temp2 = temp2.split('.')
            if len(temp2) > 2:
                baka = True
            temp2 = ''.join(temp2)

            temp = temp1 + temp2
    else:
        temp = list(pre_check[0])
        if temp[0] == '.' or temp[0] == '-' or temp[0] == "+":
            del temp[0]
        temp = ''.join(temp)

        temp = temp.split(' ')
        if len(temp) > 1:
            baka = True
        temp = ''.join(temp)
        temp = temp.split('-')
        if len(temp) > 1:
            baka = True
        temp = ''.join(temp)
        temp = temp.split('.')
        if len(temp) > 2:
            baka = True
        temp = ''.join(temp)
    return temp, baka


def easy_check(x):
    temp = start_check(x)
    if temp[1] or temp[0].isdigit() is False:
        print('Wrong value was entered!')
        exit('Invalid values')
    return float(x)


def std_round(x):
    x = '{:.7g}'.format(x)
    return x


def start_check_old(temp, baka=False):  # для шестой лабораторной
    pre_check = temp.split('e')
    if len(pre_check) > 2:
        baka = True
    elif len(pre_check) == 2:
        if pre_check[0] == '' or pre_check[1] == '':
            print('Wrong value was entered!')
            exit()
        temp1 = list(pre_check[0])
        if temp1[0] == '.' or temp1[0] == '-' or temp1[0] == "+":
            del temp1[0]
        temp1 = ''.join(temp1)

        temp1 = temp1.split(' ')
        if len(temp1) > 1:
            baka = True
        temp1 = ''.join(temp1)
        temp1 = temp1.split('-')
        if len(temp1) > 1:
            baka = True
        temp1 = ''.join(temp1)
        temp1 = temp1.split('.')
        if len(temp1) > 2:
            baka = True
        temp1 = ''.join(temp1)

        temp2 = list(pre_check[1])
        if temp2[0] == '-' or temp2[0] == "+":
            del temp2[0]
        temp2 = ''.join(temp2)
        temp2 = temp2.split(' ')
        if len(temp2) > 1:
            baka = True
        temp2 = ''.join(temp2)
        temp2 = temp2.split('-')
        if len(temp2) > 1:
            baka = True
        temp2 = ''.join(temp2)
        temp2 = temp2.split('.')
        if len(temp2) > 2:
            baka = True
        temp2 = ''.join(temp2)

        temp = temp1 + temp2
    else:
        temp = list(pre_check[0])
        if temp[0] == '.' or temp[0] == '-' or temp[0] == "+":
            del temp[0]
        temp = ''.join(temp)

        temp = temp.split(' ')
        if len(temp) > 1:
            baka = True
        temp = ''.join(temp)
        temp = temp.split('-')
        if len(temp) > 1:
            baka = True
        temp = ''.join(temp)
        temp = temp.split('.')
        if len(temp) > 2:
            baka = True
        temp = ''.join(temp)

    if baka or temp.isdigit() is False:
        print('Wrong value was entered!')
        exit('Invalid values')
    return temp
