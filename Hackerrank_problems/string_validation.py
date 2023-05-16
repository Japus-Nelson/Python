'''
Question :

You are given a string .
Your task is to find out if the string  contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

Input Format

A single line containing a string .
qA2

Output:
True
True
True
True
True

'''

if __name__ == '__main__':
    s = input()
    '''
    "any" is a built_in function "Return True if bool(x) is True for any x in the iterable
           If the iterable is empty, return False "
    '''
    print(any(k.isalnum() for k in s))
    print(any(k.isalpha() for k in s))
    print(any(k.isdigit() for k in s))
    print(any(k.islower() for k in s))
    print(any(k.isupper() for k in s))

