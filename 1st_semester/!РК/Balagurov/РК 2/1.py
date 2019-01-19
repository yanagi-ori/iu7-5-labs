# Балагуров И.С. 
# ИУ7-15Б
# Вариант 72
# Проверить можно ли из символов строки S составить строку F. 
# Предусмотреть многократный ввод строки F.

s = input('Введите базисную строку S: ')
f = ' '
print('enter - завершение выполнения программы')
if len(s)<100 :
	while True :
		f = input('Введите проверяемую строку F: ')
		if not len(f) :
			print('Завершение работы программы')
		flag = True
		for c in f:
			if s.count(c)<f.count(c) :
				print('Из букв строки {} нельзя составить строку {}'.format(s,f))
				flag = False
				break
		if flag :
			print('Из букв строки {} можно составить строку {}'.format(s,f))
else:# Дополнительный кусочек программы. Может быть еще хуже предыдущего
	while True :
		nf = f = input('Введите проверяемую строку F: ')
		if not len(f) :
			print('Завершение работы программы')
		flag = True
		while len(nf) :
			c = nf[0]
			if s.count(c)<nf.count(c) :
				print('Из букв строки {} нельзя составить строку {}'.format(s,f))
				flag = False
				break
			else:
				nf = nf.replace(c,'')
		if flag :
			print('Из букв строки {} можно составить строку {}'.format(s,f))