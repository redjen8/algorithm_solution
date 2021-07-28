from itertools import combinations

N = int(input())
arr = list(map(int, input().rstrip().split()))
arr_sum = sum(arr)
res = 0
for i in range(N-1):
    arr_sum -= arr[i]
    res += arr[i] * arr_sum
print(res)
