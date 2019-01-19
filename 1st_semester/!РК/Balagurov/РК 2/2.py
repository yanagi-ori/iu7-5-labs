# Балагуров И.С. 
# ИУ7-15Б
# Вариант 97
# По введенному названию месяца и дню недели 1го января текущего года
# Сформировать матрицу, содержащую календарь на текущий месяц.
# Разрешено использование одного дополнительного одномерного массива

def printMrx(a):
	x = len(a)
	y = len(a[0])
	for i in range(x):
		for j in range(y):
			print('{:^5}'.format(a[i][j]),end='')
		print()

print('Дни недели и названия месяцов вводить полностью, с большой буквы.')
months = month = input('Введите название месяца: ')
day = input('Введите день недели 1го января текущего года: ')
#months = month = 'Декабрь'
#day = 'Понедельник'


if month=='Январь' : month = 1
elif month=='Февраль' : month = 2
elif month=='Март' : month = 3
elif month=='Апрель' : month = 4
elif month=='Май' : month = 5
elif month=='Июнь' : month = 6
elif month=='Июль' : month = 7
elif month=='Август' : month = 8
elif month=='Сентябрь' : month = 9
elif month=='Октябрь' : month = 10
elif month=='Ноябрь' : month = 11
elif month=='Декабрь' : month = 12

if day=='Понедельник' : day = 1
if day=='Вторник' : day = 2
if day=='Среда' : day = 3
if day=='Четверг' : day = 4
if day=='Пятница' : day = 5
if day=='Суббота' : day = 6
if day=='Воскресение' : day = 7
day -= 1

days_cnt = []
days_cnt.append(31)
days_cnt.append(28)
days_cnt.append(31)
days_cnt.append(30)
days_cnt.append(31)
days_cnt.append(30)
days_cnt.append(31)
days_cnt.append(31)
days_cnt.append(30)
days_cnt.append(31)
days_cnt.append(30)
days_cnt.append(31)

#for month in range(1,13):

days_passed = 0
for i in range(month-1):
	days_passed += days_cnt[i]
	#print(day,month,days_passed)
days_passed += day
days_passed %= 7

print(months)
a = []
a.append( ['Пн','Вт','Ср','Чт','Пт','Сб','Вс'] )
curday = 0
b = ['~' for i in range(days_passed)]
while curday<days_cnt[month-1] :
	curday += 1
	b.append( str(curday) )
	if len(b)>= 7 :
		a.append(b)
		b = []
if len(b)<7 :
	while len(b)<7 :
		b.append('~')
a.append(b)

printMrx(a)
print()
print()