import sys

tree = dict()
N = 0
for line in sys.stdin:
    if line == '\n':
        break
    species = line.rstrip()
    N += 1
    if species in tree:
        tree[species] += 1
    else:
        tree[species] = 1
    
tree = sorted(tree.items(), key=lambda x:x[0])
for eachSpecies, num in tree:
    print(eachSpecies, '%.4f' %round((num/N)*100, 4))
