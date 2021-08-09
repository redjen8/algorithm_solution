S = input()
words = ['pi', 'ka', 'chu']
for x in words:
    S = S.replace(x, ' ')
for w in S:
    if w != ' ':
        print('NO')
        exit(0)
print('YES')
