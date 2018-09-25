from collections import OrderedDict

n = int(input())

orders = OrderedDict()

for i in range(n):
    info = input().split()
    name, price = " ".join(info[:-1]), int(info[-1])

    orders[name] = orders.get(name, 0) + price

for name in orders:
    print(name, orders[name])
