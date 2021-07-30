N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if j != 0:
            arr[i][j] += arr[i][j-1]

for qNum in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    res = 0
    for t in range(x1-1, x2):
        if y1 != 1:
            res -= arr[t][y1-2]
        res += arr[t][y2-1]
    print(res)
