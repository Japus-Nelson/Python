'''
Question 1 :
You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

For Example:

Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2


Answer:
'''
def swap_case(s):
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

'''
Input :  HackerRank.com presents "Pythonist 2".

Output : hACKERrANK.COM PRESENTS "pYTHONIST 2"

'''