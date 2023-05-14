'''
Task
You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.

Function Description

Complete the split_and_join function in the editor below.

split_and_join has the following parameters:

string line: a string of space-separated words

'''

def split_and_join(line):
    # write your code here
    # rstrip removes the empty space at the end of the line
    new_line = line.rstrip().replace(" ", "-")
    return new_line

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)


#  or Method: 2
a = "this is a string"
a = a.split(" ") # a is converted to a list of strings.
print(a)
a='-'.join(a)
print (a)

'''
Input : this is a string   
Output :  this-is-a-string

'''