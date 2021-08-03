T = int(input())

for i in range(T):
    N = int(input())
    zero, one, other = 1, 0, 0
    for j in range(N):
        other = one
        one += zero
        zero = other
    print(zero, one)
    