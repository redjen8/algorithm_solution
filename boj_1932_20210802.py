N = int(input())
arr = list([0] * N for _ in range(N))
for i in range(N):
    ipt = list(map(int, input().rstrip().split()))
    for j in range(i+1):
        arr[i][j] = ipt[j]
for i in range(1, N):
    for j in range(i+1):
        if j == 0:
            arr[i][j] += arr[i-1][j]
        elif j >= 1:
            arr[i][j] += max(arr[i-1][j], arr[i-1][j-1])
print(max(arr[N-1]))
