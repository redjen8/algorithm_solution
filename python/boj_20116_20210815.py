N, L = map(int, input().split())
weightX = list(map(int, input().split()))
prevCenter = weightX[N-1]
cnt = 1
for i in range(N-2, -1, -1):
    ableL, ableR = weightX[i] - L, weightX[i] + L
    if ableR < weightX[i] or weightX[i] < ableL:
        print("unstable")
        exit(0)
    if prevCenter >= weightX[i] + L or prevCenter <= weightX[i] - L:
        print("unstable")
        exit(0)
    cnt += 1
    prevCenter = (prevCenter * (cnt - 1) + weightX[i]) / cnt
print("stable")
