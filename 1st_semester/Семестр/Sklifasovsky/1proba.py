# Функция для проверки правильного ввода строки
def tryinput():
	choice = False
	while not choice:
		x = input('Введите строку > ').split()
		if len(x) != 3:
			print('Вы ввели неправильную строку')
		elif x[0] != 'H' and x[0] != 'V':
			print('1 буква введена неверно')
		else:
			try:
				a = int(x[1])
				b = int(x[2])
			except:
				print('Вы ввели некорректные числа')
			else:
				if x[0] == 'H':
					if (0 < a <= n) and (0 < b < n):
						choice = True
						return x
					else:
						print('Введены некорректные числа')
				elif x[0] == 'V':
					if (0 < a <= n) and (0 < b < n):
						choice = True
						return x
					else:
						print('Введены некорректные числа')

forinput = None
problems = 0

while forinput == None:
	maxk = 9
	problems += 1
	# Проверка на правильный ввод кол-ва точек и связующих линий
	# n - кол-во точек в ряду или столбце
	# m - кол-во связующих линий
	vvod = False
	while not vvod:
		try:
			n = int(input('Введите кол-во строк и столбцов (точек) > '))
			if 2 <= n <= 9:
				vvod = True
			else:
				print('Повторите снова, вы ввели неправильное кол-во строк'
				' (столбцов)')
		except:
			print('Вы ввели не число, повторите снова')
	vvod = False
	while not vvod:
		try: 
			m = int(input('Введите кол-во связующих линий > '))
		except:
			print('Повторите снова, вы неправильно ввели кол-во линий')
		else:
			vvod = True



	# Создаем матрицу, для работы с ней
	A = [[' ']*(2*n-1) for i in range(2*n-1)]
	newlen = 2*n-1
	for i in range(newlen):
		for j in range(newlen):
			if i % 2 == 0 and j % 2 == 0:
				A[i][j] = '#'


	# Создаем массив вводимых строк и вбиваем в него данные
	print('\nВводить данные нужно через пробел, в виде:\nV 1 1\n')
	F = ['']*m
	for x in range(m):
		F[x] = tryinput()
	print()

	# Для удобства
	for i in range(newlen):
		for j in range(newlen):
			if i % 2 != 0 and j % 2 != 0:
				A[i][j] = '!'


	# В нужных местах ставим линии
	for x in F:
		if x[0] == 'H':
			# строка
			a = 2*int(x[1])-2
			b = 2*int(x[2])-1
			A[a][b] = '━'
		elif x[0] == 'V':
			# столбец
			a = 2*(int(x[2])-1)+1
			b = 2*(int(x[1])-1)
			A[a][b] = '┃'


	# Выводим исходную матрицу
	for x in A:
		print(x)

	# Алгоритм нахождения квадратов в матрице
	newlen = len(A[0])
	# Массив для подсчета квадратов
	counts = [0 for i in range(maxk)] # Массив для количества квадратов
	for i in range(newlen):
		for j in range(newlen):
			a, b = i, j
			for z in range(maxk):
				i, j = a, b
				# Проверка линий
				if A[i][j] == '━' and (i + (z + 1) * 2) < newlen\
								  and  (j - 1 + (z + 1) * 2) < newlen:

					for k in range(z + 1):
						if A[i][j + k * 2] == A[i + (z + 1) * 2][j + k * 2] == '━'\
								 and A[i + 1 + k * 2][j - 1] ==\
								     A[i + 1 + k * 2][j - 1 + (z + 1) * 2] == '┃':

						    flag = True
						else:
							flag = False
							break

					if flag:
						counts[z] += 1


	# Выводим кол-во найденных квадратов
	counts1 = ''
	for i in counts:
		counts1 += str(i) + ' ' 
	counts1 = counts1.split()
	k = 0
	print()
	print('Проблема #', problems)
	for i in range(len(counts)):
		if counts[i] != 0:		
			print('Количество квадратов: ', (i+1), 'x', (i+1), '=', counts[i])
			k += 1
			print()
	if k == 0:
		print('Кадратов не найдено')
		print()


	# Цикл для выхода или повторного запуска программы
	forinputinside = None
	while forinputinside == None:
		forinputinside = input('Если хотите выйти - введите Да, '
								'если нет - введите Нет > ')
		if forinputinside == 'Да':
			forinput = 0
		elif forinputinside == 'Нет':
			forinput = None
		else:
			print('Повторите снова, вы неправильно ввели')
			forinputinside = None