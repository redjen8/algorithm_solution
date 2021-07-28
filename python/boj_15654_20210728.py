from itertools import permutations

N, M = map(int, input().split())
arr = list(map(int, input().rstrip().split()))
arr.sort()
res_set = permutations(arr, M)
for x in res_set:
    for each in x:
        print(each, end=' ')
    print()
