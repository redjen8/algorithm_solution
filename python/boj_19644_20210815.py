arr = [0] * 3000001
head, tail = 0, 0
L = int(input())
gunRange, gunPower = map(int, input().split())
mineNum = int(input())
acc = 0
for i in range(L):
    enemy = int(input())
    acc += gunPower
    if enemy > acc :
        if not mineNum:
            print('NO')
            exit(0)
        else:
            mineNum -= 1
            acc -= gunPower
            arr[tail] = 0
            tail += 1
    else:
        arr[tail] = 0
        tail += 1
    if tail - head >= gunRange:
        acc -= arr[head]
        head += 1
print('YES')
