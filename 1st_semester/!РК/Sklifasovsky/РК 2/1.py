S = input('Введите строку S без пробелов! > ')
n = int(input('Введите кол-во строк F > '))
st = ''
for i in range(n):
	st += input('Введите строку F > ') + ' '
st = st.split()
print(S)
for x in st:
	S1 = S
	x1 = x
	for y in S1:
		if y in x:
			S1 = S1.replace(y, '')
			x = x.replace(y, '')
	print(x, ' , ', S1,x == '')
	if x == '':
		print('Строку ', x1, ' можно')
	else:
		print('Строку ', x1, 'нельзя')

d = 'bbb'
g = d.replace('b','a')
print(g)