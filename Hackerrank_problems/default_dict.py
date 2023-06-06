from collections import defaultdict


d = defaultdict(list)
m, n = list(map(int, input().split()))

# getting the string and index position on the dict list
for i in range(m):
    d[input()].append(str(i+1))

# getting the string position of group B in group A:
for j in range(n):
    print(" ".join(d[input()]) or -1)

