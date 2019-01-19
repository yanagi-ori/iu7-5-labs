n = input('Вводить в формате: месяц/деньнедели1-гоянваря > ')
n = n.split('/')
print(n)
# Пока что только с январем
q = 6
q1 = 7
A = []
for i in range(q):
	A += [[0]*7]

if n[1] == 'Понедельник':
	for i in range(q):
		for j in range(q1):
			A[0][j] = j+1
if n[1] == 'Вторник':
	for i in range(q):
		for j in range(q1):
			A[0][j] = j
if n[1] == 'Среда':
	for i in range(q):
		for j in range(q1):
			A[0][j] = j-1
if n[1] == 'Четверг':
	for i in range(q):
		for j in range(q1):
			A[0][j] = j-2
if n[1] == 'Пятница':
	for i in range(q):
		for j in range(q1):
			A[0][j] = j-3
if n[1] == 'Суббота':
	for i in range(q):
		for j in range(q1):
			A[0][j] = j-4
if n[1] == 'Воскресенье':
	for i in range(q):
		for j in range(q1):
			A[0][j] = j-5

t = A[0][6]
for i in range(1, q):
	for j in range(q1):
		t += 1
		A[i][j] = t



for i in range(q):
	for j in range(q1):
		if not 0 < A[i][j] <= 31:
			A[i][j] = 0

for i in range(q):
	for j in range(q1):
		print('{:3}'.format(A[i][j]), end=' ')
	print()