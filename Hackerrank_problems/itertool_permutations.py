'''
“Permutation” it refers to all the possible combinations in which a set or string can be ordered or arranged.
 
 Similarly here itertool.permutations() method provides us with all the possible arrangements
 that can be there for an iterator

and all elements are assumed to be unique on the "basis of their position" and not by their value or category.\

SAMPLE INPUT:
HACK 2

Sample Output

AC
AH
AK
CA
CH
CK
HA
HC
HK
KA
KC
KH
'''


from itertools import permutations


string, size = input().split()
size = int(size)

# String should always be upper regardless of input
string = string.upper()

# Permutation:
output = list(sorted(permutations(string, size)))
# print(output)

# Convert list of tuples to list of string:
str = [''.join(i) for i in output]

# Print the desired output
for i in str:
    print(i)