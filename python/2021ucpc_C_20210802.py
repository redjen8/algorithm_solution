a, d, k = map(int, input().split())
turn = 1
win = d / 100
r, res = 1, 0
while win < 1:
    res += win * r * turn * a / 100
    r *= 1 - win
    win += win * k / 100
    turn += 1
res += r * turn * a / 100
print("{:.7f}".format(res*100)) 
