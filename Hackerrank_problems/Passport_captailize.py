# !/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    new_l = list(s.rstrip().splitlines())
    # "Prints all the input as a one string and add it to the list"
    l = "".join(new_l)
    # seperates the each string in a list
    new = l.split(" ")
    li = []
    for i in new:
        n  = i.capitalize()
        li.append(n)
    return " ".join(li)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    '''
    export OUTPUT_PATH = "file path"
    export OUTPUT_PATH="/c/Users/japus/PycharmProjects/pythonProject/path_file.txt"
    '''

    s = input()

    result = (solve(s))
    print(result)

    fptr.write(result)

    fptr.close()

'''
You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, alison heck should be capitalised correctly as Alison Heck.


Given a full name, your task is to capitalize the name appropriately.

Input Format

A single line of input containing the full name, .

Constraints

The string consists of alphanumeric characters and spaces.
Note: in a word only the first character is capitalized. Example 12abc when capitalized remains 12abc.

Output Format

Print the capitalized string, .

Sample Input

chris alan
Sample Output

Chris Alan


'''