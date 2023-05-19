'''

Given an integer, , print the following values for each integer  from  to :

Decimal
Octal
Hexadecimal (capitalized)
Binary

INPUT:
5

Output:
  1   1   1   1
  2   2   2  10
  3   3   3  11
  4   4   4 100
  5   5   5 101
'''


def print_formatted(number):
    # your code goes here
    w = len(bin(n)[2:])
    # print(w)
    for i in range(1, number+1):
        # print(oct(i))
        print(str(i).rjust(w),
              oct(i).replace("0o","").rjust(w),
              hex(i).upper().replace('0X', '').rjust(w),
              bin(i).replace('0b', '').rjust(w)
              )



if __name__ == '__main__':
    n = int(input())
    print_formatted(n)


