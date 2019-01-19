def srezprobelov(m):
    count = 0
    for x in m:
        ln = len(x)
        i, j = 0, 0
        k, k1 = 0, 0
        while x[i] == ' ':
            i += 1
            k += 1
        while x[ln - 1 - j] == ' ':
            k1 += 1
            j += 1
        m[count] = None
        m[count] = x[k:ln - k1]
        count += 1
    return m


m = [
        '       Заметался пожар голубой, позабылись',
        '  родимые дали. В первый',
        'раз я запел про любовь. В первый',
        ' раз отрекаюсь скандалить. Был я',
        'весь как запущеный сад,',
        'был на женщин и зелия ',
        'падок. Разонравилось пить я плясать',
        'и терять свою жизнь без оглядки.'
        ]
m = srezprobelov(m)
sogl = 'бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦ'
t = ''
for x in m:
	t += (x + ' ')
t = t.split('.')

print(t)
print()
maxslovo = ''
q = 0
p = 0
st = ''
numstroki = None
for x in t:

	x += ' '
	slovo = ''
	for c in x:
		if c != ' ':
			slovo += c
		else:
			if slovo != '':
				k = 0
				for i in slovo:
					if i in sogl:
						k += 1
					if k >= p:
						p = k
						maxslovo = slovo
						st = x
				slovo = ''	
znaki = '.,;:'
maxslovo1 = ''
for x in maxslovo:
	if x in znaki:
		pass
	else:
		maxslovo1 += x
maxslovo = maxslovo1

print('В предложении:', st, '\nМаксимальное слово:', maxslovo )