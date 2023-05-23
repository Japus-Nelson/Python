from itertools import product
# a = input().split()
# b = input().split()
a = map(int, input().split())
b = map(int, input().split())
print(*product(a,b))

