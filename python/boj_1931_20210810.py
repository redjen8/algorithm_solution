from sys import stdin
N = int(stdin.readline())
conference = list()
for i in range(N):
    a, b = map(int, input().split())
    conference.append([a, b])
conference.sort(key=lambda x:(x[1],x[0]))
res, bnd = 0, 0
for i in range(N):
    if bnd <= conference[i][0]:
        res += 1
        bnd = conference[i][1]

print(res)
