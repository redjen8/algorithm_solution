from itertools import permutations
N = int(input())
K = int(input())
arr = list(input().rstrip() for _ in range(N))
possibleNum = set()
for x in permutations(arr, K):
    itr = ""
    for items in x:
        itr += items
    possibleNum.add(itr)
print(len(possibleNum))
