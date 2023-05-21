'''
Question : Print the alphabetr rangoli

i/p : 0<n<26

o/p : abc..z rangoli
'''

def print_rangoli(size):
    # your code goes here

    for i in range(size-1, -1, -1):
        for j in range(i):
            print(end="--")
        for j in range(size-1, i, -1):
            print(chr(j+97), end='-')
        for j in range(i, size):
            if j != size -1 :
                print(chr(j+97), end='-')
            else:
                print(chr(j+97), end='')
        for j in range(2*i):
            print(end='-')
        print()

    for i in range(1, size):
        for j in range(i):
            print(end='--')
        for j in range(size-1, i, -1):
            print(chr(j+97), end='-')
        for j in range(i, size):
            if j != size-1:
                print(chr(j+97), end='-')
            else:
                print(chr(j+97), end='')
        for j in range(2*i):
            print(end='-')
        print()


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

# print(chr(5+97))
' 0 - 25 --> a-z '


'''
--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
'''

