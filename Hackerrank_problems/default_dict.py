from collections import defaultdict

m, n = list(map(int, input().split()))

m_list = defaultdict(list)
for i in range(1, m+1):
    m_list[i].append((input()))
# print(m_list)

n_list = []
for j in range(1,n+1):
    n_list.append(input())
# print(n_list)


d = defaultdict(list)
for i in n_list:
    for j in range(1, len(m_list)+1):
        if i in m_list[j]:
            # print(i)
            # print(m_list[j])
            # print(j)
            d[i].append(j)

for i in range(1, len(d.items())+1):
    print(i)
    print(d)









