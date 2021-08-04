N = int(input())
for i in range(N):
    ipt = list(input().rstrip().split())
    res = "god"
    for l in range(1, len(ipt)):
        res += ipt[l]
    print(res)
