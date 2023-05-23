def merge_the_tools(string, k):
    # your code goes here
    # print(len(string))
    for i in range(0, len(string), k):
        t1 = (string[i:i+k])
        u1 = []
        for j in t1:
            if j in t1:
                if j not in u1:
                    u1.append(j)
        # print(u1)
        print("".join(u1))




if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)


# if 'a'