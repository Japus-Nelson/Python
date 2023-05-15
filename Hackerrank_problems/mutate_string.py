'''
We have seen that lists are mutable (they can be changed), and tuples are immutable (they cannot be changed).

Let's try to understand this with an example.

You are given an immutable string, and you want to make changes to it.
'''


def mutate_string(string, position, character):
    l = list(string)
    # print(l)
    l[position] = character
    # print(l)
    s = ''.join(l)
    return s


if __name__ == '__main__':
    s = input()  # input()
    i, c = input().split()  # input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)


'''
Input:
abracadabra
5
k

Output:
abrackdabra
'''

