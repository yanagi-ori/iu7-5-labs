# 112 вариант
# Богатырев Иван


def month():
    month_num = input('Введите название месяца: ')
    month_num.lower().replace('январь', '0')
    month_num.lower().replace('Февраль', '1')
    month_num.lower().replace('март', '2')
    month_num.lower().replace('апрель', '3')
    month_num.lower().replace('май', '4')
    month_num.lower().replace('июнь', '5')
    month_num.lower().replace('июль', '6')
    month_num.lower().replace('август', '7')
    month_num.lower().replace('сентябрь', '8')
    month_num.lower().replace('октябрь', '9')
    month_num.lower().replace('ноябрь', '10')
    month_num.lower().replace('декабрь', '11')
    try:
        month_num = int(month_num)
    except ValueError:
        print('Такого месяца не существует. Попробуйте снова.')
        month()
    return month_num


def day_of_the_week():
    day = input('Введите день недели 1-го января: ')
    day.lower().replace('понедельник', '0')
    day.lower().replace('вторник', '1')
    day.lower().replace('среда', '2')
    day.lower().replace('четверг', '3')
    day.lower().replace('пятница', '4')
    day.lower().replace('суббота', '5')
    day.lower().replace('воскресенье', '6')
    try:
        day = int(day)
    except ValueError:
        print('Такого месяца не существует. Попробуйте снова.')
        day_of_the_week()
    return day

calendar = [[], [], [], [], []]
day = day_of_the_week()
m = month()
year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days_sum = sum(year[:m])
ost = (days_sum % 7 + day) % 7
for i in range(ost):
    calendar[0].append(' ')
for i in range(7 - ost):
    for week in range(5):
        pass
