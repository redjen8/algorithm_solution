N = int(input())
craneWeightLimit = list(map(int, input().rstrip().split()))
M = int(input())
boxWeight = list(map(int, input().rstrip().split()))

craneWeightLimit.sort(reverse=True)
boxWeight.sort(reverse=True)
res = 0

if craneWeightLimit[0] < boxWeight[0]:
    print(-1)
    exit(0)
else:
    while boxWeight:
        res += 1
        for eachCrane in craneWeightLimit:
            if not boxWeight:
                break
            else:
                for i in range(len(boxWeight)):
                    if boxWeight[i] <= eachCrane:
                        boxWeight.pop(i)
                        break

print(res)