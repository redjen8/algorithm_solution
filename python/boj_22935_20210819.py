T = int(input())
strawberry = list(i for i in range(1, 16))
for i in range(14, 0, -1):
    strawberry.append(i)
for i in range(len(strawberry)):
    a = str(bin(strawberry[i]))[2:]
    a = '%4s' % a
    a = a.replace(' ', '0')
    a = a.replace('0', 'V')
    a = a.replace('1', '딸기')
    strawberry[i] = a
strawberry.pop()
for i in range(T):
    tc = int(input())
    print(strawberry[(tc-1)%28])