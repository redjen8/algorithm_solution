X1, Y1, Z1, X2, Y2, Z2 = map(int, input().split())
N = int(input())
stickLength = list(map(int, input().split()))
dist = ((X2-X1)**2 + (Y2-Y1)**2 + (Z2-Z1)**2 ) ** 0.5
if 2*max(stickLength) - sum(stickLength) <= dist <= sum(stickLength):
    print('YES')
else:
    print('NO')
