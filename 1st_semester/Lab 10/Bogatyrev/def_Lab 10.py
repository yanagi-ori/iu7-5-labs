OUTPUT = open('output.txt', 'w')
OUTPUT.close()
OUTPUT = open('output.txt', 'a')
len_source = 0
with open('TEST_TEXT.txt') as SOURCE:
    for line in SOURCE:
        len_source += 1

cur = 0
for i in range(len_source, -1, -1):
    with open('TEST_TEXT.txt') as SOURCE:
        for line in SOURCE:
            if cur == i:
                OUTPUT.write(line)
            cur += 1
    cur = 0
OUTPUT.close()
