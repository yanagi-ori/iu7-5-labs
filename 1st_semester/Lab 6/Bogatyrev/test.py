from sys import exit

baka = False
check = ''
final = []
n = input('Задача №1\nВведите размер массива: ')
n_t = n.split('e')
if len(n_t) == 2:
    if n_t[0] == '' or n_t[1] == '':
        print('Wrong value was entered!')
        exit()
    if n_t[1][0] == '+':
        start = list(n_t[1])
        del start[0]
        n_t[1] = ''.join(start)
n_t = ''.join(n_t)
if n.isdigit() or n_t.isdigit():
    print('Введите значения массива (по одному):')
    n = int(float(n))
    orig_m = [0]*n
    for i in range(n):
        temp = input()
        orig_m[i] = temp
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
else:
    print('Wrong value was entered!')
    exit()