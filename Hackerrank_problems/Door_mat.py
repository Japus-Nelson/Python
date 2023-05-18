'''
Question :

Input Format

A single line containing the space separated values of  and .

Constraints

Output Format

Output the design pattern.

Sample Input

9 27
Sample Output

------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------

'''

n, m = map(int, input().split())
# print(n, m)

# Top cone :
for i in range(1, n, 2):
    print((i * ".|.").center(m, "-"))

# Mid Tier :
print(('WELCOME').center(m, "-"))

# Bottom part :
for i in range(n-2, 0, -2):
    print((i * ".|.").center(m, '-'))


'''
Size: 7 x 21 

    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------
'''
