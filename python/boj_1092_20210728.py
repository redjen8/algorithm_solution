N = int(input())
craneWeightLimit = list(map(int, input().rstrip().split()))
M = int(input())
boxWeight = list(map(int, input().rstrip().split()))

craneWeightLimit.sort()
boxWeight.sort()
res = 0
craneAvailable = [1] * N

for boxIdx in range(M):
    for craneIdx in range(N):
        if craneAvailable[craneIdx]:
            if boxWeight[boxIdx] <= craneWeightLimit[craneIdx]:
                craneAvailable[craneIdx] = 0
                break
            else:
                continue
        else:
            continue
    if sum(craneAvailable) == 0:
        res += 1
        craneAvailable = [1] * N
        continue
    if boxIdx != M-1 and craneIdx == N-1:
        print(-1)
        exit(0)

if boxIdx == M-1:
    res += 1
print(res)
