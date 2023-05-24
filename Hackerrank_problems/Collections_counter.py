from collections import Counter

no_shoes = list(map(int, input().split()))
shoe_sizes = list(map(int, input().split()))
cr = Counter(shoe_sizes).items()
no_customers = int(input())
am_earned = []
for i in range(1, no_customers+1):
    sh_sz, price = list(map(int, input().split()))
    # print(sh_sz, price)
    if sh_sz in shoe_sizes:
        am_earned.append(price)
        shoe_sizes.remove(sh_sz)
        # print(Counter(shoe_sizes).items())
print(sum(am_earned))



'''
10 
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50

Customer 1: Purchased size 6 shoe for $55.
Customer 2: Purchased size 6 shoe for $45.
Customer 3: Size 6 no longer available, so no purchase.
Customer 4: Purchased size 4 shoe for $40.
Customer 5: Purchased size 18 shoe for $60.
Customer 6: Size 10 not available, so no purchase.

Total money earned =  

QN: 
The first line contains , the number of shoes.
The second line contains the space separated list of all the shoe sizes in the shop.
The third line contains , the number of customers.
The next  lines contain the space separated values of the  desired by the customer and , the price of the shoe.

'''

