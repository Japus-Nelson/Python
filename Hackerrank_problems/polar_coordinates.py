import cmath

c = complex(input())

#absolute value of the complex
absolute = abs(c)
print(absolute)

# convert to polar co-ordinates
d = cmath.phase(c)
print(d)


'''
input : 1+2j

output :

2.23606797749979
1.1071487177940904


'''