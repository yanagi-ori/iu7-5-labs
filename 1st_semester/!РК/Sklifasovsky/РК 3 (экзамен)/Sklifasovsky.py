def transport():
	path = input('Введите путь ')
	f = open(path, 'r')
	F = []
	for line in f:
		st = [line.rstrip()]
		for i in st:
			st2 = []
			for x in i:
				st2 += [x]
			F += [st2]
	f.close()
	M = len(F)
	N = len(F[0])
	for i in range(M):
		N = min(N, len(F[i]))
	A = []
	print()
	for i in range(N):
		st = []
		for j in range(M):
			st += [F[j][i]]
		A += [st]

	for i in range(N):
		for j in range(M):
			print(A[i][j], end=' ')
		print()
	return A, N, M

def delete(F, N, M):
	for i in range(N):
		st1 = []
		st2 = []
		t = None
		for j in range(M):
			if j+1 < N and i < M: 
				st1 += [F[j][i]]
				st2 += [F[j+1][i]]
				if st1 == st2:
					t = j

		if t != None:
			for i in range(N):
				for j in range(M):
					F[i][t+1] = None
	print(F)
	for i in range(N):
		for j in range(M):
			if F[i][j] != None:
				print(F[i][j], end=' ')
		print()





A, N, M = transport()	
delete(A, N, M)


