'''
Question:

In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.

NOTE: String letters are case-sensitive.

Input Format

The first line of input contains the original string. The next line contains the substring.

Constraints


Each character in the string is an ascii character.

Output Format

Output the integer number indicating the total number of occurrences of the substring in the original string.

Sample Input

ABCDCDC
CDC
Sample Output

2
'''


def count_substring(string1, sub_string1):
    str_len = len(string1)
    sub_len = len(sub_string1)
    count = 0
    for i in range(0, len(string)):
        for j in range(sub_len, (1 + str_len)):
            # Check every len(substring) in the string starting from 0 to len(string)
            if string[i:j] == sub_string:      # string slicing = [start:stop:stepover]
                count +=1
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)