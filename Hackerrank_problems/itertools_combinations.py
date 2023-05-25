'''
Similarly itertools.combinations() provides us with all the possible tuples a sequence or set of numbers or
letters used in the iterator

and the elements are assumed to be unique on the basis of their positions which are distinct for all elements
'''


from itertools import combinations

string, size = input().upper().split()
size = int(size)

for n in range(1, size+1):
    output = [ i for i in (combinations(sorted(string), n))]
    # print(output)

    str = [''.join(i) for i in output]
    print("\n".join(str))
