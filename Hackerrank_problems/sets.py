def average(array):
    # your code goes here
    # print(array)
    array = set(array)
    length = len(array)
    return (sum(array) / length)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)


'''
Now, let's use our knowledge of sets and help Mickey.

Ms. Gabriel Williams is a botany professor at District College. One day, she asked her student Mickey to compute the average of all the plants with distinct heights in her greenhouse.

Formula used:

Function Description

Complete the average function in the editor below.

average has the following parameters:

int arr: an array of integers

QN : 
input:
10
161 182 161 154 176 170 167 171 170 174

168.6
'''